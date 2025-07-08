from datetime import date, timedelta
from typing import List

from sqlalchemy import select, func, case
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import (
    ExceptionInfrastructureType,
)
from src.common.infrastructure.infrastructure_exception.infrastructure_exception import (
    InfrastructureException,
)
from src.common.utils.result import Result

from src.dashboard.application.dtos.request.get_occupacy_percentage_request_dto import GetOccupancyPercentageRequestDto
from src.dashboard.application.enum.period_type import PeriodType
from src.dashboard.application.dtos.request.get_reservation_count_request_dto import (
    GetReservationCountRequestDTO,
)
from src.dashboard.application.dtos.response.get_reservation_count_response_dto import (
    GetReservationCountResponseDTO,
)
from src.dashboard.application.dtos.request.get_top_dishes_preorder_request_dto import (
    GetTopDishesPreorderRequestDTO,
)
from src.dashboard.application.dtos.response.get_top_dishes_preorder_response_dto import (
    GetTopDishesPreorderRequestDTO as TopDishesResponseDTO,
)

from src.dashboard.application.dtos.response.get_occupacy_percentage_response_dto import (
    GetOccupancyPercentageResponseDto,
)
from src.dashboard.application.repositories.query.dashboard_query_repository import (
    IDashboardQueryRepository,
)
from src.reservation.infraestructure.models.orm_reservation_model import OrmReservationModel
from src.restaurant.infraestructure.models.orm_table_model import OrmTableModel
from src.menu.infrastructure.models.menu_model import DishModel  # placeholder


class OrmDashboardQueryRepository(IDashboardQueryRepository):
    """
    SQLAlchemy implementation of dashboard queries.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_reservations_count(
        self, dto: GetReservationCountRequestDTO
    ) -> Result[GetReservationCountResponseDTO]:
        """
        Count reservations for today or the last 7 days.
        """
        try:
            today = date.today()

            if dto.period_type == PeriodType.DAY:
                start_date = today
            else:  # WEEK
                start_date = today - timedelta(days=7)

            stmt = select(func.count().label("cnt")).where(
                OrmReservationModel.reservation_date.between(start_date, today)
            )
            result = await self.session.execute(stmt)
            count = result.scalar_one()

            response = GetReservationCountResponseDTO(
                period_type=dto.period_type, count=count
            )
            return Result.success(response)

        except InfrastructureException as ie:
            return Result.fail(ie)
        except Exception as e:
            return Result.fail(
                InfrastructureException(str(e), infra_type=ExceptionInfrastructureType.UNKNOWN)
            )

    async def get_top_preordered_dishes(
        self, dto: GetTopDishesPreorderRequestDTO
    ) -> Result[List[TopDishesResponseDTO]]:
        """
        Returns the top N pre-ordered dishes.
        Assumes there's an ORM model DishModel with fields
        dish_id, dish_name.
        """
        try:
            stmt = (
                select(
                    DishModel.id,
                    DishModel.name,
                    func.count().label("total_preorders"),
                )
                .group_by(
                    DishModel.id,
                    DishModel.name,
                )
                .order_by(func.count().desc())
                .limit(dto.top_n)
            )
            result = await self.session.execute(stmt)
            rows = result.all()

            dishes = [
                TopDishesResponseDTO(
                    dish_id=row.id,
                    dish_name=row.name,
                    total_preorders=row.total_preorders,
                )
                for row in rows
            ]
            return Result.success(dishes)

        except InfrastructureException as ie:
            return Result.fail(ie)
        except Exception as e:
            return Result.fail(
                InfrastructureException(str(e), infra_type=ExceptionInfrastructureType.BAD_REQUEST)
            )

    async def get_occupancy_percentage_by_restaurant(
        self, dto: GetOccupancyPercentageRequestDto
    ) -> Result[List[GetOccupancyPercentageResponseDto]]:
        """
        Calculates occupancy percent per restaurant for the current month.
        """
        try:
            today = date.today()
            first_of_month = today.replace(day=1)

            # Subquery: total tables per restaurant
            tables_subq = (
                select(
                    OrmTableModel.restaurant_id.label("res_id"),
                    func.count().label("total_tables"),
                )
                .group_by(OrmTableModel.restaurant_id)
                .subquery()
            )

            # Subquery: distinct occupied tables (via reservations) per restaurant
            occ_subq = (
                select(
                    OrmReservationModel.restaurant_id.label("res_id"),
                    func.count(func.distinct(OrmReservationModel.table_number_id)).label(
                        "occupied_tables"
                    ),
                )
                .where(
                    OrmReservationModel.reservation_date.between(first_of_month, today)
                )
                .group_by(OrmReservationModel.restaurant_id)
                .subquery()
            )

            # Join restaurants + aggregates
            stmt = (
                select(
                    tables_subq.c.res_id,
                    tables_subq.c.total_tables,
                    func.coalesce(occ_subq.c.occupied_tables, 0).label("occupied_tables"),
                )
                .join(
                    occ_subq,
                    tables_subq.c.res_id == occ_subq.c.res_id,
                    isouter=True,
                )
                .offset(dto.offset)
                .limit(dto.limit)
            )
            result = await self.session.execute(stmt)
            rows = result.all()

            response = []
            for row in rows:
                percent = (
                    row.occupied_tables / row.total_tables * 100
                    if row.total_tables > 0
                    else 0.0
                )
                # fetch restaurant name (could be joined; using ORMReservationModel as placeholder)
                name_stmt = select(OrmReservationModel.restaurant_name).where(
                    OrmReservationModel.restaurant_id == row.res_id
                )
                name_res = await self.session.execute(name_stmt)
                restaurant_name = name_res.scalar_one()

                response.append(
                    GetOccupancyPercentageResponseDto(
                        restaurant_id=row.res_id,
                        restaurant_name=restaurant_name,
                        occupied_tables=row.occupied_tables,
                        total_tables=row.total_tables,
                        occupancy_percent=percent,
                    )
                )

            return Result.success(response)

        except InfrastructureException as ie:
            return Result.fail(ie)
        except Exception as e:
            return Result.fail(
                InfrastructureException(str(e), infra_type=ExceptionInfrastructureType.BAD_REQUEST)
            )

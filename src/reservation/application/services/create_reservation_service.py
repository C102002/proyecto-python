from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.application import IService
from src.common.application.id_generator.id_generator import IIdGenerator
from src.common.utils import Result
from src.reservation.application.dtos.request.create_reservation_request_dto import CreateReservationRequest
from src.reservation.application.dtos.response.create_reservation_response_dto import CreateReservationResponse
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from src.reservation.domain.aggregate.reservation import Reservation
from src.reservation.domain.value_objects.reservation_date_end_vo import ReservationDateEndVo
from src.reservation.domain.value_objects.reservation_date_start_vo import ReservationDateStartVo
from src.reservation.domain.value_objects.reservation_date_vo import ReservationDateVo
from src.reservation.domain.value_objects.reservation_id_vo import ReservationIdVo
from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo
from src.restaurant.domain.entities.value_objects.table_number_id_vo import TableNumberId
from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

class CreateReservationService(IService[CreateReservationRequest, CreateReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        command_reser: IReservationCommandRepository,
        #query_restau: IRestaurantQueryRepository,
        id_generator: IIdGenerator
        ):
        super().__init__()
        self.query_repository = query_reser
        self.command_repository = command_reser
        self.id_generator = id_generator
        #self.query_restau = query_restau
        
    async def execute(self, value: CreateReservationRequest) -> Result[CreateReservationResponse]:
        
        # MAximo cuatro horas por reserva
        if ( value.date_end - value.date_start > 4 ):
            raise Exception("Maximo cuatro horas por reserva")
        
        # MESA DISPONIBLE. No pueden haber mas de dos reservas activas para la misma mesa en el mismo horario
        findTable = await self.query_repository.exists_by_table(
            table_id=value.table_number_id,
            date_start=value.date_start,
            date_end=value.date_end,
            reservation_date=value.reservation_date,
            restaurant_id = value.restaurant_id
        )
        if (findTable.value == True):
            raise Exception("Mesa no disponible")
        
        # Cliente reserva activa en el mismo horario, incluso si son en diferentes restaurantes
        findReser = await self.query_repository.exists_by_date_client(
            date_start= value.date_start, 
            date_end= value.date_end, 
            reservation_date= value.reservation_date, 
            client_id= value.client_id
        )
        if (findReser.value == True ):
            raise Exception("Cliente ya posee una reserva activa en el mismo horario")
        
        # Horario de reserva debe estar dentro del horario de apertura, cierre del restarurante
        
        # Los platos deben pertenecer al menu del restaurante de la mesa reservada
        
        # Proceso
        id = await self.id_generator.generate_id()
        
        self.command_repository.save(
            Reservation(
                client_id=UserIdVo(value.client_id),
                id=ReservationIdVo(id),
                date_end=ReservationDateEndVo(value.date_end),
                date_start=ReservationDateStartVo(value.date_start),
                reservation_date=ReservationDateVo(value.reservation_date),
                status=ReservationStatusVo("pendiente"),
                table_number_id=TableNumberId(value.table_number_id),
                restaurant_id=RestaurantIdVo(value.restaurant_id)
            )
        )
        
        response = CreateReservationResponse(id=id)
        return Result.success(response)


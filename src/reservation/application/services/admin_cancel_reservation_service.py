from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.admin_cancel_reservation_request_dto import AdminCancelReservationRequest
from src.reservation.application.dtos.response.admin_cancel_reservation_response_dto import AdminCancelReservationResponse
from src.reservation.application.exceptions.cancel_order_not_pending_exception import CancelOrderNotPendingException
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository

from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo

class AdminCancelReservationService(IService[AdminCancelReservationRequest, AdminCancelReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        command_reser: IReservationCommandRepository,
        ):
        super().__init__()
        self.query_repository = query_reser
        self.command_repository = command_reser
        
    async def execute(self, value: AdminCancelReservationRequest) -> Result[AdminCancelReservationResponse]:
        
        find = await self.query_repository.get_by_id(id=value.reservation_id)
        if (find.is_success == False):
            return Result.fail(find.error) 
        
        result = find.value
        
        print(f"result:{result.status.reservation_status}")
        
        # NO se puede cancelar una reserva que ya paso
        if not result.status.equals(ReservationStatusVo("pendiente")):
            return Result.fail(CancelOrderNotPendingException())
        
        result.update_status_cancelada()
        await self.command_repository.update(result)
        response = AdminCancelReservationResponse()
        return Result.success(response)


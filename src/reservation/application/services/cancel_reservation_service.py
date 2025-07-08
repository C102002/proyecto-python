from src.auth.domain.value_objects.user_id_vo import UserIdVo
from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest
from src.reservation.application.dtos.response.cancel_reservation_response_dto import CancelReservationResponse
from src.reservation.application.exceptions.cancel_order_not_owned_exception import CancelOrderNotOwnedExeption
from src.reservation.application.exceptions.cancel_order_not_pending_exception import CancelOrderNotPendingException
from src.reservation.application.exceptions.cancel_order_not_time_allowed_exception import CancelOrderTooLateException
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from datetime import datetime

from src.reservation.domain.value_objects.reservation_status_vo import ReservationStatusVo

class CancelReservationService(IService[CancelReservationRequest, CancelReservationResponse]):

    def __init__(
        self,    
        query_reser: IReservationQueryRepository, 
        command_reser: IReservationCommandRepository,
        ):
        super().__init__()
        self.query_repository = query_reser
        self.command_repository = command_reser
        
    async def execute(self, value: CancelReservationRequest) -> Result[CancelReservationResponse]:
        hora_actual = datetime.now().time()
                
        find = await self.query_repository.get_by_id(id=value.reservation_id)
                
        if (find.is_success == False):
            return Result.fail(find.error)
        
        
        result = find.value
        
        hora_reserva = result.date_start
        
        print(f"cliente {result.client_id}")
        
 
        # UN cliente solo puede cancelar sus reservas
        if not result.client_id.equals(UserIdVo(value.client_id)) :
            return Result.fail(CancelOrderNotOwnedExeption())     
        
        # CLiente no puede cancelar 1 hora antes
        horaA = hora_reserva.reservation_date_start.hour * 60 + hora_reserva.reservation_date_start.hour
        horaB = hora_actual.hour * 60 + hora_actual.minute
        minutosRestantes = horaA-horaB
        if (minutosRestantes < 1):
            minutosRestantes = minutosRestantes*-1

        if minutosRestantes < 60:
            return Result.fail(CancelOrderTooLateException())
        
        # UN cliente un puede cancelar una reserva que ya paso
        if not result.status.equals(ReservationStatusVo("pendiente")):
            return Result.fail(CancelOrderNotPendingException())
        
        # ADmin puede cancelar cuando quiera
        result.update_status_cancelada()
        update_response=await self.command_repository.update(result)
        
        
        if update_response.is_error:
            return Result.fail(update_response.error)
        
        response = CancelReservationResponse()
        return Result.success(response)


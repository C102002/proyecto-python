from src.common.application import IService
from src.common.utils import Result
from src.reservation.application.dtos.request.cancel_reservation_request_dto import CancelReservationRequest
from src.reservation.application.dtos.response.cancel_reservation_response_dto import CancelReservationResponse
from src.reservation.application.repositories.command.reservation_command_repository import IReservationCommandRepository
from src.reservation.application.repositories.query.reservation_query_repository import IReservationQueryRepository
from datetime import datetime

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
            raise find.error
 
        result = find.value
        hora_reserva = result.date_start
 
        # UN cliente solo puede cancelar sus reservas
        if result.client_id != value.client_id:
            raise Exception("No puede cancelar reservas que no son suyas")       
        
        # CLiente no puede cancelar 1 hora antes
        horaA = hora_reserva.hour * 60 + hora_reserva.minute
        horaB = hora_actual.hour * 60 + hora_actual.minute
        minutosRestantes = horaA-horaB
        if (minutosRestantes < 1):
            minutosRestantes = minutosRestantes*-1

        if minutosRestantes < 60:
            raise Exception("No puede cancelar 1 hora antes")
        
        # UN cliente un puede cancelar una reserva que ya paso
        if result.status != "pendiente":
            raise Exception("No es posible cancelar dicha reserva")
        
        # ADmin puede cancelar cuando quiera
        result.update_status_cancelada()
        await self.command_repository.update(result)
        response = CancelReservationResponse()
        return Result.success(response)


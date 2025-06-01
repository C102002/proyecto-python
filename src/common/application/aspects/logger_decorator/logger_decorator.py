from typing import Generic, TypeVar
from src.common.utils import Result
from ...decorators.base_service_decorator import BaseServiceDecorator
from ...service.service import IService
from ...logger.logger import ILogger
from ...timer.timer import ITimer

I = TypeVar('I')
O = TypeVar('O')

class LoggerDecorator(BaseServiceDecorator[I, O], Generic[I, O]):
    def __init__(self, service: IService[I, O], logger: ILogger, timer: ITimer):
        super().__init__(service)
        self.logger = logger
        self.timer = timer

    async def execute(self, value: I) -> Result[O]:
        begining_time = self.timer.set_time()
        data = await self.service.execute(value)
        ending_time = self.timer.set_time()
        time = self.timer.get_time(begining_time, ending_time)

        if data.is_error:
            self.logger.error_log(
                self.service.class_name,
                str(data.error),
                str(value),
                f"{time}ms",
                getattr(data.error, "stacks", [])
            )
        else:
            self.logger.success_log(
                self.service.class_name,
                str(value),
                f"{time}ms"
            )

        return data
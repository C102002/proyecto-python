import logging
from src.common.application import ILogger

class FastAPILogger(ILogger):
    def __init__(self):
        # No se si funcione bien
        self.logger = logging.getLogger("fastapi")

    def success_log(self, service_name: str, input: str, time: str) -> None:
        self.logger.info(f"Successful execute: -- Input: {input} -- Time: {time}", extra={"service": service_name})

    def error_log(self, service_name: str, message: str, input: str, time: str, cause: list[str]) -> None:
        self.logger.error(
            f"Error execute: Error: {message} -- Input: {input} -- Time: {time} -- StackTrace: {cause}",
            extra={"service": service_name}
        )
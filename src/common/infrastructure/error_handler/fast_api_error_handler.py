import logging
from fastapi import HTTPException, status

from src.common.application.error_handler.error_handler import IErrorHandler
from src.common.domain.domain_exception.domain_exception import DomainException
from src.common.infrastructure.infrastructure_exception.enum.infraestructure_exception_type import (
    ExceptionInfrastructureType
)
from src.common.infrastructure.infrastructure_exception.infrastructure_exception import (
    InfrastructureException
)
from src.common.application.application_exception.application_exception import ApplicationException
from src.common.application.application_exception.enum.application_exception_type import ExceptionApplicationType
from src.common.utils.base_exception import BaseException
from src.common.utils.base_exception_enum import BaseExceptionEnum
from src.restaurant.domain.domain_exceptions.invalid_table_number_id import InvalidTableNumberIdException


class FastApiErrorHandler(IErrorHandler):

    def _handle_domain_exception(self,error:DomainException, message: str) -> Exception:
        if isinstance(error,InvalidTableNumberIdException):
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

    def _handle_application_exception(
        self,
        error: ApplicationException, 
        message: str
    ) -> Exception:
        logging.debug(f"ENTER _handle_application_exception: {error!r}, {message!r}")
        app_type = error.get_application_type()

        if app_type == ExceptionApplicationType.CONFLICT:
            code = status.HTTP_409_CONFLICT
        elif app_type == ExceptionApplicationType.FORBIDDEN:
            code = status.HTTP_403_FORBIDDEN
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
        
        return HTTPException(status_code=code, detail=message)

    def _handle_infrastructure_exception(
        self,
        error: InfrastructureException,
        message: str
    ) -> Exception:
        logging.debug(f"ENTER _handle_infrastructure_exception: {error!r}, {message!r}")
        infra_type = error.get_infrastructure_type()

        if infra_type == ExceptionInfrastructureType.BAD_REQUEST:
            code = status.HTTP_400_BAD_REQUEST
        elif infra_type == ExceptionInfrastructureType.CONFLICT:
            code = status.HTTP_409_CONFLICT
        elif infra_type == ExceptionInfrastructureType.NOT_FOUND:
            code = status.HTTP_404_NOT_FOUND
        elif infra_type == ExceptionInfrastructureType.PERSISTENCE:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif infra_type == ExceptionInfrastructureType.UNAUTHORIZED:
            code = status.HTTP_401_UNAUTHORIZED
        elif infra_type == ExceptionInfrastructureType.INTERNAL_SERVER_ERROR:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif infra_type == ExceptionInfrastructureType.USER_NOT_FOUND:
            code = status.HTTP_404_NOT_FOUND
        else:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR
            message = "Unexpected infrastructure error"

        return HTTPException(status_code=code, detail=message)

    def to_http(self, error: BaseException, message: str) -> Exception:
        print(f"error del mapper: {error!r}")
        if error.type == BaseExceptionEnum.DOMAIN_EXCEPTION:
            return self._handle_domain_exception(error,message)
        elif error.type == BaseExceptionEnum.APPLICATION_EXCEPTION:
            if isinstance(error, ApplicationException):
                return self._handle_application_exception(error, message)
            else:
                return HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid application exception"
                )
        elif error.type == BaseExceptionEnum.INFRASTRUCTURE_EXCEPTION:
            if isinstance(error, InfrastructureException):
                return self._handle_infrastructure_exception(error, message)
            else:
                return HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Invalid infrastructure exception"
                )
        else:
            return HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected error"
            )
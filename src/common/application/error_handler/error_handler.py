from abc import ABC, abstractmethod
from src.common.utils.base_exception import BaseException

class IErrorHandler(ABC):
    """
    Interfaz que define cómo convertir nuestras excepciones de dominio,
    aplicación e infraestructura en HTTPException de FastAPI.
    """

    @abstractmethod
    def to_http(self,exception:BaseException,message: str) -> Exception:
        pass
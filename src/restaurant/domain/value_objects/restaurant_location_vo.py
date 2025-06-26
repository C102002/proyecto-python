from src.common.domain import ValueObjectRoot
from src.restuarant.domain.domain_exceptions.invalid_location_longitude_exception import InvalidLocationLongitudeException
from ..domain_exceptions.invalid_location_latitude_exception import InvalidLocationLatitudeException
import re

class RestaurantLocationVo(ValueObjectRoot["RestaurantLocationVo"]):
    
    def __init__(self, lat: float, lng:float):
        regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not -90.0 <= lat <=  90.0:
            raise InvalidLocationLatitudeException(
                f"Latitud inválida: {lat}. Debe estar entre -90 y 90."
            )

        if not -180.0 <= lng <= 180.0:
            raise InvalidLocationLongitudeException(
                f"Longitud inválida: {lng}. Debe estar entre -180 y 180."
            )
        
        self.lat = lat
        self.lng = lng

    def equals(self, value: "RestaurantLocationVo") -> bool:
        return (self.lat == value.lat) and (self.lng == value.lng)

    
    @property
    def lat(self) -> float:
        return self.lat

    @property
    def lng(self) -> float:
        return self.lng
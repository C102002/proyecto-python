from src.common.domain.entity.entity_root import EntityRoot
from src.menu.domain.value_objects.dish_id_vo import DishIdVo
from src.menu.domain.value_objects.dish_name_vo import DishNameVo
from src.menu.domain.value_objects.dish_description_vo import DishDescriptionVo
from src.menu.domain.value_objects.dish_price_vo import DishPriceVo
from src.menu.domain.value_objects.dish_category_vo import DishCategoryVo
from src.menu.domain.value_objects.dish_image_vo import DishImageVo

class Dish(EntityRoot[DishIdVo]):

    def __init__(self, id: DishIdVo, name: DishNameVo, description: DishDescriptionVo, price: DishPriceVo, category: DishCategoryVo, image: DishImageVo = None, is_available: bool = True):
        super().__init__(id)
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.is_available = is_available

    def update_name(self, name: DishNameVo):
        self.name = name

    def update_description(self, description: DishDescriptionVo):
        self.description = description

    def update_price(self, price: DishPriceVo):
        self.price = price

    def update_category(self, category: DishCategoryVo):
        self.category = category

    def update_image(self, image: DishImageVo):
        self.image = image

    def set_available(self):
        self.is_available = True

    def set_unavailable(self):
        self.is_available = False

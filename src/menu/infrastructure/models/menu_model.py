from typing import List, Optional
from sqlalchemy import Column, String, Float, Boolean, Table, ForeignKey
from sqlmodel import Field, Relationship, SQLModel

from src.common.infrastructure.database import Base
from src.menu.domain.aggregate.menu import Menu
from src.menu.domain.entities.dish import Dish
from src.restaurant.infraestructure.models.orm_restaurant_model import OrmRestaurantModel

menu_dish_association = Table(
    'menu_dish_association',
    Base.metadata,
    Column('menu_id', String, ForeignKey('menus.id')),
    Column('dish_id', String, ForeignKey('dishes.id'))
)

class DishModel(SQLModel, table=True):
    __tablename__ = 'dishes'

    id: str = Field(primary_key=True, index=True)
    name: str = Field(index=True)
    description: str
    price: float
    category: str
    image: Optional[str] = None
    is_available: bool = Field(default=True)
    menu_id: Optional[str] = Field(default=None, foreign_key="menus.id")

    menu: "MenuModel" = Relationship(back_populates="dishes")

    @staticmethod
    def from_domain(dish: "Dish"):
        return DishModel(
            id=str(dish.id.value),
            name=dish.name.value,
            description=dish.description.value,
            price=dish.price.value,
            category=dish.category.value,
            image=dish.image.value if dish.image else None,
            is_available=dish.is_available
        )

    def to_domain(self) -> "Dish":
        from src.menu.domain.value_objects.dish_id_vo import DishIdVo
        from src.menu.domain.value_objects.dish_name_vo import DishNameVo
        from src.menu.domain.value_objects.dish_description_vo import DishDescriptionVo
        from src.menu.domain.value_objects.dish_price_vo import DishPriceVo
        from src.menu.domain.value_objects.dish_category_vo import DishCategoryVo
        from src.menu.domain.value_objects.dish_image_vo import DishImageVo

        return Dish(
            id=DishIdVo(self.id),
            name=DishNameVo(self.name),
            description=DishDescriptionVo(self.description),
            price=DishPriceVo(self.price),
            category=DishCategoryVo(self.category),
            image=DishImageVo(self.image) if self.image else None,
            is_available=self.is_available
        )

class MenuModel(SQLModel, table=True):
    __tablename__ = 'menus'

    id: str = Field(primary_key=True, index=True)
    restaurant_id: str = Field(foreign_key='restaurant.id')

    dishes: List["DishModel"] = Relationship(back_populates="menu")

    @staticmethod
    def from_domain(menu: "Menu"):
        menu_model = MenuModel(id=str(menu.id.value), restaurant_id=str(menu.restaurant_id.restaurant_id))
        menu_model.dishes = [DishModel.from_domain(dish) for dish in menu.dishes]
        return menu_model

    def to_domain(self) -> "Menu":
        from src.menu.domain.value_objects.menu_id_vo import MenuIdVo
        from src.restaurant.domain.value_objects.restaurant_id_vo import RestaurantIdVo

        return Menu(
            id=MenuIdVo(self.id),
            restaurant_id=RestaurantIdVo(self.restaurant_id),
            dishes=[dish.to_domain() for dish in self.dishes],
            categories=[] # Categories are not persisted in this example
        )

    def update_from_domain(self, menu: "Menu"):
        incoming_dish_map = {str(d.id.value): d for d in menu.dishes}
        
        dishes_to_remove = []
        for db_dish in self.dishes:
            if db_dish.id not in incoming_dish_map:
                dishes_to_remove.append(db_dish)

        for dish_to_del in dishes_to_remove:
            self.dishes.remove(dish_to_del)

        for domain_dish_id, domain_dish_data in incoming_dish_map.items():
            found_existing_dish = next((d for d in self.dishes if d.id == domain_dish_id), None)

            if found_existing_dish:
                found_existing_dish.name = domain_dish_data.name.value
                found_existing_dish.description = domain_dish_data.description.value
                found_existing_dish.price = domain_dish_data.price.value
                found_existing_dish.category = domain_dish_data.category.value
                found_existing_dish.image = domain_dish_data.image.value if domain_dish_data.image else None
                found_existing_dish.is_available = domain_dish_data.is_available
            else:
                new_dish_model = DishModel.from_domain(domain_dish_data)
                self.dishes.append(new_dish_model)

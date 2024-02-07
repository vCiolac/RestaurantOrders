import csv
from typing import List

from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self._load_menu_data()

    def _load_menu_data(self) -> List[Dish]:
        with open(self.source_path, 'r') as file:
            reader = csv.DictReader(file)
            return self._add_dishes(reader)

    def _add_dishes(self, reader: csv.DictReader) -> List[Dish]:
        dishes = []
        for dish_data in reader:
            dish_name = dish_data.get('dish')
            dish_price = float(dish_data.get('price', 0))
            ingredient_name = dish_data.get('ingredient')
            ingredient_amount = int(dish_data.get('recipe_amount', 0))

            if dish_name:
                dish = self._handle_dish(dishes, dish_name, dish_price)
                if ingredient_name:
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name),
                        ingredient_amount,
                        )
        return dishes

    def _handle_dish(
            self,
            dishes: List[Dish],
            dish_name: str,
            dish_price: float,
            ) -> Dish:
        for dish in dishes:
            if dish.name == dish_name:
                return dish
        new_dish = Dish(dish_name, dish_price)
        dishes.append(new_dish)
        return new_dish

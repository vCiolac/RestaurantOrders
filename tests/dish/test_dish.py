from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish('Pizza', 45.0)
    assert dish.name == 'Pizza'
    assert dish.price == 45.0
    assert dish.recipe == {}

    with pytest.raises(TypeError):
        Dish('Pizza', '15.0')

    with pytest.raises(ValueError):
        Dish('Pizza', -15.0)

    dish2 = Dish('Lasanha', 35.0)
    dish3 = Dish('Lasanha', 35.0)
    assert dish != dish2
    assert dish2 == dish3
    assert repr(dish2) == "Dish('Lasanha', R$35.00)"

    assert hash(dish2) == hash(dish3)
    assert hash(dish) != hash(dish2)

    farinha = Ingredient('farinha de trigo')
    tomate = Ingredient('tomate')
    queijo_mussarela = Ingredient('queijo mussarela')
    queijo_parmesao = Ingredient('queijo parmesão')
    queijo_provolone = Ingredient('queijo provolone')
    queijo_gorgonzola = Ingredient('queijo gorgonzola')

    dish.add_ingredient_dependency(farinha, 1)
    dish.add_ingredient_dependency(tomate, 1)
    dish.add_ingredient_dependency(queijo_mussarela, 1)
    dish.add_ingredient_dependency(queijo_parmesao, 1)
    dish.add_ingredient_dependency(queijo_provolone, 1)
    dish.add_ingredient_dependency(queijo_gorgonzola, 1)

    assert farinha in dish.recipe
    assert tomate in dish.recipe
    assert queijo_mussarela in dish.recipe
    assert queijo_parmesao in dish.recipe
    assert queijo_provolone in dish.recipe
    assert queijo_gorgonzola in dish.recipe

    assert dish.recipe[farinha] == 1
    assert dish.recipe[tomate] == 1
    assert dish.recipe[queijo_mussarela] == 1
    assert dish.recipe[queijo_parmesao] == 1
    assert dish.recipe[queijo_provolone] == 1
    assert dish.recipe[queijo_gorgonzola] == 1

    assert dish.get_ingredients() == {
        farinha,
        tomate,
        queijo_mussarela,
        queijo_parmesao,
        queijo_provolone,
        queijo_gorgonzola,
        }

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        }

from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient = Ingredient('queijo parmesão')
    assert ingredient.name == 'queijo parmesão'

    assert ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE
        }

    ingredient2 = Ingredient('queijo parmesão')
    ingredient3 = Ingredient('presunto')

    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)

    assert ingredient != ingredient3
    assert ingredient == ingredient2

    assert repr(ingredient) == "Ingredient('queijo parmesão')"

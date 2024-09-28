from shopping_cart import Item, ShoppingCart
import pytest

@pytest.mark.slow
@pytest.mark.windows
def test_add():
    result = 2 + 2
    assert result == 4

@pytest.mark.xfail
def test_mult():
    result = 2 * 3
    assert result == 6


@pytest.mark.slow
def test_get_all_items(cart):
    milk = Item("Milk", 2)
    apple = Item("Apple", 1)

    cart.add_item(milk)
    cart.add_item(apple)

    assert cart.get_items() == ["Milk", "Apple"]

@pytest.mark.slow
def test_get_all_sum(cart):
    milk = Item("Milk", 2)
    apple = Item("Apple", 1)
    apple2 = Item("Apple3", 1)

    cart.add_item(milk)
    cart.add_item(apple)
    cart.add_item(apple2)

    assert cart.get_items() == ["Milk", "Apple", "Apple3"]


@pytest.mark.windows
def test_remove_item(cart):
    milk = Item("Milk", 2)
    apple = Item("Apple", 1)

    cart.add_item(milk)
    cart.add_item(apple)
    cart.remove_item("Apple")

    assert cart.get_items() == ["Milk"]

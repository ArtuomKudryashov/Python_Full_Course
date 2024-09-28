import pytest
from shopping_cart import  ShoppingCart

@pytest.fixture()
def cart():
    cart = ShoppingCart()
    print("Подготовка к тесту...")
    # return  cart

    yield cart
    #
    print("После теста...")
    # #
    cart.clear()

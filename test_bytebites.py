from models import Customer, MenuItem, Menu, Order


import pytest

from models import Customer, MenuItem, Menu, Order


def test_calculate_total_with_multiple_items():
    burger = MenuItem("Spicy Burger", 10.00, "Food", 4.8)
    soda = MenuItem("Large Soda", 3.00, "Drinks", 4.5)

    order = Order([burger, soda])

    assert order.calculate_total() == pytest.approx(13.00)


def test_order_total_is_zero_when_empty():
    order = Order()

    assert order.calculate_total() == 0


def test_filter_menu_items_by_category():
    menu = Menu()

    burger = MenuItem("Spicy Burger", 10.00, "Food", 4.8)
    soda = MenuItem("Large Soda", 3.00, "Drinks", 4.5)
    cake = MenuItem("Chocolate Cake", 5.00, "Desserts", 4.9)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    result = menu.filter_by_category("Drinks")

    assert [item.name for item in result] == ["Large Soda"]


def test_filter_category_ignores_capitalization():
    menu = Menu()
    soda = MenuItem("Large Soda", 3.00, "Drinks", 4.5)
    menu.add_item(soda)

    result = menu.filter_by_category("drinks")

    assert [item.name for item in result] == ["Large Soda"]


def test_sort_menu_by_popularity():
    menu = Menu()

    burger = MenuItem("Spicy Burger", 10.00, "Food", 4.8)
    soda = MenuItem("Large Soda", 3.00, "Drinks", 4.5)
    cake = MenuItem("Chocolate Cake", 5.00, "Desserts", 4.9)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    result = menu.sort_by_popularity()

    assert [item.name for item in result] == [
        "Chocolate Cake",
        "Spicy Burger",
        "Large Soda",
    ]


def test_menu_rejects_non_menu_items():
    menu = Menu()

    with pytest.raises(TypeError):
        menu.add_item("Spicy Burger")


def test_negative_menu_item_price_is_rejected():
    with pytest.raises(ValueError):
        MenuItem("Spicy Burger", -10.00, "Food", 4.8)


def test_customer_purchase_history():
    customer = Customer("Alex")
    burger = MenuItem("Spicy Burger", 10.00, "Food", 4.8)
    order = Order([burger])

    customer.add_purchase(order)

    assert customer.name == "Alex"
    assert len(customer.purchase_history) == 1
    assert customer.purchase_history[0] is order

import pytest
from order import Order
from menu_item import MenuItem


def test_create_order_initial_state():
    order = Order(1)

    assert order.order_number == 1
    assert order.items == []
    assert isinstance(order.timestamp, object)  # timestamp deve ser datetime
    assert order.total_price == 0.0
    assert order.status == "Em Preparação"


def test_add_item_and_calculate_total():
    order = Order(1)
    ramen = MenuItem("Lamen", "Prato", 30.0)
    drink = MenuItem("Suco", "Bebida", 10.0)

    order.add_item(ramen, 2)
    order.add_item(drink, 1)

    assert len(order.items) == 2
    assert order._calculate_total_price() == 70.0


def test_add_item_invalid_quantity():
    order = Order(1)
    ramen = MenuItem("Lamen", "Prato", 30.0)

    with pytest.raises(ValueError, match="A quantidade deve ser maior que zero."):
        order.add_item(ramen, 0)


def test_update_status_valid():
    order = Order(1)

    order.update_status("Pronto")
    assert order.status == "Pronto"

    order.update_status("Retirado")
    assert order.status == "Retirado"


def test_update_status_invalid():
    order = Order(1)

    with pytest.raises(ValueError, match="Status inválido"):
        order.update_status("Cancelado")


def test_get_details_returns_dict():
    order = Order(1)
    ramen = MenuItem("Lamen", "Prato", 30.0)
    order.add_item(ramen, 2)

    details = order.get_details()

    assert details["order_number"] == 1
    assert details["items_quantity"] == 1
    assert details["total_price"] == 60.0
    assert details["status"] == "Em Preparação"


def test_str_representation_contains_info():
    order = Order(1)
    ramen = MenuItem("Lamen", "Prato", 30.0)
    order.add_item(ramen, 2)

    string = str(order)

    assert "Order Number: 1" in string
    assert "Lamen (x2)" in string
    assert "Total Price: $60.00" in string
    assert "Status: Em Preparação" in string

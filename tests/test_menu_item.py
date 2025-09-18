import pytest
from menu_item import MenuItem


def test_create_menu_item_valid():
    item = MenuItem("Lamen", "Prato", 25.0)

    assert item.name == "Lamen"
    assert item.type == "Prato"
    assert item.price == 25.0


def test_set_price_valid():
    item = MenuItem("Suco", "Bebida", 8.0)
    item.price = 10.0
    assert item.price == 10.0


def test_set_price_invalid_raises():
    item = MenuItem("Água", "Bebida", 5.0)
    with pytest.raises(ValueError, match="O preço não pode ser negativo."):
        item.price = -2.0


def test_get_info_returns_dict():
    item = MenuItem("Guioza", "Entrada", 15.0)
    info = item.get_info()

    assert info == {
        "name": "Guioza",
        "type": "Entrada",
        "price": 15.0
    }


def test_str_representation():
    item = MenuItem("Lamen", "Prato", 30.0)
    string = str(item)

    assert "Product name: Lamen" in string
    assert "Product type: Prato" in string
    assert "Price: 30.0" in string

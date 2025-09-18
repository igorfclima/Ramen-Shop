import pytest
from ramen_shop_system import RamenShopSystem
from kitchen import Kitchen
from cash_register import CashRegister
from order import Order
from menu_item import MenuItem


class FakeKitchen(Kitchen):
    def __init__(self):
        self.processed_orders = []

    def process_order(self, order: Order) -> None:
        order.update_status("Pronto")
        self.processed_orders.append(order)


class FakeCashRegister(CashRegister):
    def __init__(self):
        super().__init__()
        self.recorded = []

    def record_order(self, order: Order) -> None:
        self.recorded.append(order)


def test_load_and_display_menu(capsys):
    system = RamenShopSystem(FakeKitchen(), FakeCashRegister())

    system.display_menu()
    captured = capsys.readouterr()

    assert "🍜 MENU DO RAMEN SHOP 🍜" in captured.out
    assert "TAMANHOS:" in captured.out
    assert "PROTEÍNAS:" in captured.out
    assert "BEBIDAS:" in captured.out


def test_get_menu_item_returns_correct_item():
    system = RamenShopSystem(FakeKitchen(), FakeCashRegister())
    item = system.get_menu_item("Bebida", "Água")

    assert isinstance(item, MenuItem)
    assert item.name == "Água"
    assert item.type == "Bebida"
    assert item.price == 1.50


def test_create_order_increments_number():
    system = RamenShopSystem(FakeKitchen(), FakeCashRegister())

    order1 = system.create_order()
    order2 = system.create_order()

    assert order1.order_number == 1
    assert order2.order_number == 2


def test_place_and_process_order():
    kitchen = FakeKitchen()
    system = RamenShopSystem(kitchen, FakeCashRegister())
    order = system.create_order()

    system.place_order_in_queue(order)
    assert len(system.order_queue) == 1

    processed = system.process_next_order()
    assert processed.status == "Pronto"
    assert processed in kitchen.processed_orders
    assert len(system.order_queue) == 0


def test_process_next_order_returns_none_when_empty():
    system = RamenShopSystem(FakeKitchen(), FakeCashRegister())

    result = system.process_next_order()
    assert result is None


def test_mark_order_as_picked_up_success():
    kitchen = FakeKitchen()
    cash_register = FakeCashRegister()
    system = RamenShopSystem(kitchen, cash_register)

    order = system.create_order()
    order.update_status("Pronto")
    system.place_order_in_queue(order)

    success = system.mark_order_as_picked_up(order.order_number)

    assert success is True
    assert order in cash_register.recorded
    assert order.status == "Retirado"


def test_mark_order_as_picked_up_fails_if_not_ready():
    system = RamenShopSystem(FakeKitchen(), FakeCashRegister())

    order = system.create_order()
    # ainda "Em Preparação"
    system.place_order_in_queue(order)

    success = system.mark_order_as_picked_up(order.order_number)
    assert success is False

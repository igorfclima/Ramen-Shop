import pytest
from cash_register import CashRegister
from order import Order


class FakeOrder(Order):
    """Mock simples de Order para os testes."""
    def __init__(self, total_price: float):
        self.total_price = total_price
        self.status = "Novo"

    def update_status(self, new_status: str) -> None:
        self.status = new_status


def test_cash_register_starts_empty():
    register = CashRegister()
    assert register.orders == []
    assert register.calculate_daily_balance() == {
        "total_orders": 0,
        "total_value": 0,
        "average_ticket": 0.0
    }


def test_record_order_updates_status_and_adds_order():
    register = CashRegister()
    order = FakeOrder(50.0)

    register.record_order(order)

    # Pedido deve estar no registro
    assert order in register.orders
    # Status deve ter mudado
    assert order.status == "Retirado"


def test_calculate_daily_balance_with_orders():
    register = CashRegister()
    order1 = FakeOrder(40.0)
    order2 = FakeOrder(60.0)

    register.record_order(order1)
    register.record_order(order2)

    balance = register.calculate_daily_balance()

    assert balance["total_orders"] == 2
    assert balance["total_value"] == 100.0
    assert balance["average_ticket"] == 50.0


def test_print_balance(capsys):
    register = CashRegister()
    order = FakeOrder(30.0)
    register.record_order(order)

    register.print_balance()
    captured = capsys.readouterr()

    assert "Balanço Diário:" in captured.out
    assert "Total de Pedidos: 1" in captured.out
    assert "Receita Total: R$ 30.00" in captured.out
    assert "Ticket Médio: R$ 30.00" in captured.out

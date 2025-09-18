import pytest
from kitchen import Kitchen
from order import Order


class FakeOrder(Order):
    """Mock de Order para os testes."""
    def __init__(self, order_number: int):
        self.order_number = order_number
        self.status = "Novo"

    def update_status(self, new_status: str) -> None:
        self.status = new_status


def test_process_order_updates_status_and_notifies(monkeypatch, capsys):
    kitchen = Kitchen()
    order = FakeOrder(1)

    # Evita o delay real do sleep
    monkeypatch.setattr("kitchen.sleep", lambda x: None)

    # Executa
    kitchen.process_order(order)

    # Status deve ter mudado
    assert order.status == "Pronto"

    # Captura a saída do print
    captured = capsys.readouterr()
    assert "Processando pedido 1..." in captured.out
    assert "Preparando..." in captured.out
    assert "Pedido pronto!" in captured.out
    assert "Pedido 1 está pronto para retirada!" in captured.out


def test_notify_ready_prints_message(capsys):
    kitchen = Kitchen()
    order = FakeOrder(2)

    kitchen.notify_ready(order)

    captured = capsys.readouterr()
    assert "Pedido 2 está pronto para retirada!" in captured.out

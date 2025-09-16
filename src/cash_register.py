from typing import Dict
from order import Order


class CashRegister:
    """Gerencia os registros financeiros e o balanço do restaurante."""
    @property
    def orders(self) -> list[Order]:
        return self._orders

    def __init__(self) -> None:
        """Construtor da classe CashRegister."""
        self._orders = []

    def record_order(self, order: Order) -> None:
        """Adiciona um pedido (marcado como 'Retirado') ao balanço diário."""
        order.update_status("Retirado")
        self._orders.append(order)

    def calculate_daily_balance(self) -> Dict[str, float | int]:
        """
        Calcula e retorna um dicionário com o balanço do dia.
        Inclui: total de pedidos, receita total e ticket médio.
        """
        return {
            "total_orders": len(self._orders),
            "total_value": sum(order.total_price for order in self._orders),
            "average_ticket": (sum(order.total_price for order in self._orders) / len(self._orders)) if self._orders else 0.0
        }

    def print_balance(self) -> None:
        """Exibe no console um relatório formatado do balanço diário."""
        balance = self.calculate_daily_balance()
        print("Balanço Diário:")
        print(f"Total de Pedidos: {balance['total_orders']}")
        print(f"Receita Total: R$ {balance['total_value']:.2f}")
        print(f"Ticket Médio: R$ {balance['average_ticket']:.2f}")

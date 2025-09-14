from typing import Dict
from order import Order


class CashRegister:
    """Gerencia os registros financeiros e o balanço do restaurante."""

    def __init__(self) -> None:
        """Construtor da classe CashRegister."""
        pass

    def record_order(self, order: Order) -> None:
        """Adiciona um pedido (marcado como 'Retirado') ao balanço diário."""
        pass

    def calculate_daily_balance(self) -> Dict[str, float | int]:
        """
        Calcula e retorna um dicionário com o balanço do dia.
        Inclui: total de pedidos, receita total e ticket médio.
        """
        pass

    def print_balance(self) -> None:
        """Exibe no console um relatório formatado do balanço diário."""
        pass

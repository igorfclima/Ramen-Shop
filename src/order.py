from datetime import datetime
from typing import Dict
from menu_item import MenuItem


class Order:
    """Representa um único pedido feito por um cliente."""

    @property
    def order_number(self) -> int:
        return self.__order_number
    @property
    def items(self) -> list[tuple[MenuItem, int]]:
        return self.__items
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    @property
    def total_price(self) -> float:
        return self.__total_price
    @property
    def status(self) -> str:
        return self.__status

    def __init__(self, order_number: int) -> None:
        """Construtor da classe Order."""
        self.__order_number = order_number
        self.__items = []
        self.__timestamp = datetime.now()
        self.__total_price = 0.0
        self.__status = "Em Preparação"

    def add_item(self, item: MenuItem) -> None:
        """Adiciona um MenuItem ao pedido e recalcula o preço total."""
        pass

    def _calculate_total_price(self) -> float:
        """(Método interno) Calcula o preço total com base nos itens da lista."""
        pass

    def update_status(self, new_status: str) -> None:
        """
        Atualiza o status do pedido.
        Ex: "Em Preparação", "Pronto", "Retirado".
        """
        pass

    def get_details(self) -> Dict[str, any]:
        """Retorna um dicionário com todos os detalhes do pedido."""
        pass

    def __str__(self) -> str:
        """Retorna uma representação em string do pedido."""
        pass

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

    def add_item(self, item: MenuItem, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.__items.append((item, quantity))

    def _calculate_total_price(self) -> float:
        """(Método interno) Calcula o preço total com base nos itens da lista."""
        return sum(item.price * quantity for item, quantity in self.__items)

    def update_status(self, new_status: str) -> None:
        """
        Atualiza o status do pedido.
        Ex: "Em Preparação", "Pronto", "Retirado".
        """
        options = ["Em Preparação", "Pronto", "Retirado"]
        if new_status not in options:
            raise ValueError(f"Status inválido. Opções válidas: {options}")
        self.__status = new_status

    def get_details(self) -> Dict[str, any]:
        """Retorna um dicionário com todos os detalhes do pedido."""
        return {
            "order_number": self.__order_number,
            "data": self.timestamp,
            "items_quantity": len(self.__items),
            "total_price": self._calculate_total_price(),
            "status": self.__status
        }

    def __str__(self) -> str:
        """Retorna uma representação em string do pedido."""
        items_str = "\n".join([f"{item.name} (x{quantity}) - ${item.price * quantity:.2f}" for item, quantity in self.__items])
        return (f"Order Number: {self.__order_number}\n"
                f"Timestamp: {self.__timestamp}\n"
                f"Items:\n{items_str}\n"
                f"Total Price: ${self._calculate_total_price():.2f}\n"
                f"Status: {self.__status}")

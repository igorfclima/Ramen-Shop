from typing import Dict
from menu_item import MenuItem


class Order:
    """Representa um único pedido feito por um cliente."""

    def __init__(self, order_number: int) -> None:
        """Construtor da classe Order."""
        pass

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

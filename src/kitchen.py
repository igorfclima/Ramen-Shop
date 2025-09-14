from order import Order


class Kitchen:
    """Responsável por simular a preparação dos pedidos."""

    def __init__(self) -> None:
        """Construtor da classe Kitchen."""
        pass

    def process_order(self, order: Order) -> None:
        """
        Recebe um pedido, simula o preparo e atualiza seu status para 'Pronto'.
        """
        pass

    def notify_ready(self, order: Order) -> None:
        """Notifica que um pedido específico está pronto para retirada."""
        pass

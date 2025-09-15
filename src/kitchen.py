from time import time
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
        print(f"Processando pedido {order.order_number}...")
        print("Preparando...")
        time.sleep(2)
        print("Pedido pronto!")
        order.update_status("Pronto")
        self.notify_ready(order)

    def notify_ready(self, order: Order) -> None:
        """Notifica que um pedido específico está pronto para retirada."""
        print(f"Pedido {order.order_number} está pronto para retirada!")

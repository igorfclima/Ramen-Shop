from typing import Optional
from cash_register import CashRegister
from kitchen import Kitchen
from menu_item import MenuItem
from order import Order


class RamenShopSystem:
    """
    Classe central que coordena todas as outras. Orquestra o fluxo de pedidos.
    """

    @property
    def menu_data(self) -> dict[str, list[MenuItem]]:
        return self.__menu_data
    @property
    def order_queue(self) -> list[Order]:
        return self.__order_queue
    @property
    def next_order_number(self) -> int:
        return self.__next_order_number
    @property
    def kitchen(self) -> Kitchen:
        return self.__kitchen
    @property
    def cash_register(self) -> CashRegister:
        return self.__cash_register

    def __init__(self, kitchen: Kitchen, cash_register: CashRegister) -> None:
        """
        Construtor que utiliza Injeção de Dependência para Kitchen e CashRegister.
        """
        self.__kitchen = kitchen
        self.__cash_register = cash_register
        self.__menu_data = {}
        self.__order_queue = []
        self.__next_order_number = 1

    def _load_menu(self) -> None:
        """(Método interno) Carrega os dados do menu a partir de uma fonte."""
        menu_items = {
            "Tamanhos": [
                MenuItem("Pequeno", "Tamanho", 8.00),
                MenuItem("Médio", "Tamanho", 10.00),
                MenuItem("Grande", "Tamanho", 12.00),
            ],
            "Proteínas": [
                MenuItem("Carne de Porco", "Proteína", 3.00),
                MenuItem("Frango", "Proteína", 2.50),
                MenuItem("Tofu", "Proteína", 2.00),
                MenuItem("Camarão", "Proteína", 4.00),
            ],
            "Adicionais": [
                MenuItem("Ovo Cozido", "Adicional", 1.50),
                MenuItem("Alga Nori", "Adicional", 1.00),
                MenuItem("Cebolinha", "Adicional", 0.50),
                MenuItem("Milho", "Adicional", 1.00),
                MenuItem("Broto de Bambu", "Adicional", 1.50),
                MenuItem("Cogumelo Shiitake", "Adicional", 2.00),
            ],
            "Bebidas": [
                MenuItem("Chá Verde", "Bebida", 3.00),
                MenuItem("Refrigerante", "Bebida", 2.50),
                MenuItem("Água", "Bebida", 1.50),
                MenuItem("Suco de Laranja", "Bebida", 3.50),
            ],
        }

        self.__menu_data = menu_items


    def _generate_order_number(self) -> int:
        """(Método interno) Gera um número de pedido novo e único."""
        pass

    def display_menu(self) -> None:
        """Exibe o menu de forma organizada para o cliente."""
        if not self.__menu_data:
            self._load_menu()

        print("=" * 50)
        print("🍜 MENU DO RAMEN SHOP 🍜")
        print("=" * 50)

        for category, items in self.__menu_data.items():
            print(f"\n{category.upper()}:")
            print("-" * (len(category) + 1))
            for item in items:
                print(f"  • {item.name:<20} R$ {item.price:.2f}")

        print("\n" + "=" * 50)

    def get_menu_item(self, item_type: str, item_name: str) -> Optional[MenuItem]:
        """Busca e retorna um MenuItem específico do menu."""
        if not self.__menu_data:
            self._load_menu()

        for category, items in self.__menu_data.items():
            for item in items:
                if item.type.lower() == item_type.lower() and item.name.lower() == item_name.lower():
                    return item

        return None

    def create_order(self) -> Order:
        """Cria uma nova instância de Order com um número único."""
        order = Order(self.__next_order_number)
        self.__next_order_number += 1
        return order

    def place_order_in_queue(self, order: Order) -> None:
        """Coloca um pedido finalizado pelo cliente na fila de espera da cozinha."""
        self.__order_queue.append(order)

    def process_next_order(self) -> Optional[Order]:
        """
        Pega o próximo pedido da fila, envia para a cozinha processar
        e o retorna. Retorna None se a fila estiver vazia.
        """
        if self.__order_queue:
            next_order = self.__order_queue.pop(0)
            self.__kitchen.process_order(next_order)
            return next_order
        return None

    def _locate_order_by_number(self, order_number: int) -> Optional[Order]:
        for order in self.__order_queue:
            if order.order_number == order_number:
                return order

    def mark_order_as_picked_up(self, order_number: int) -> bool:
        """
        Encontra um pedido pelo número, atualiza seu status para 'Retirado'
        e o registra no caixa. Retorna True se for bem-sucedido.
        """
        located_order = self._locate_order_by_number(order_number)
        if located_order and located_order.status == "Pronto":
            located_order.update_status("Retirado")
            self.__cash_register.record_order(located_order)
            return True
        return False

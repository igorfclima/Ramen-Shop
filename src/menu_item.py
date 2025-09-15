class MenuItem:
    """Representa um item do menu (tamanho, proteína, adicional, etc.)."""

    def __init__(self, name: str, item_type: str, price: float) -> None:
        self.__name = name
        self.__type = item_type
        self.price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def type(self) -> str:
        return self.__type

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__price = value

    def get_info(self) -> dict[str, object]:
        """Retorna um dicionário com as informações do item."""
        return {
            "name": self.__name,
            "type": self.__type,
            "price": self.__price
        }

    def __str__(self) -> str:
        """Retorna uma representação em string do item."""
        return f"Product name: {self.__name}\nProduct type: {self.__type}\nPrice: {self.__price}"

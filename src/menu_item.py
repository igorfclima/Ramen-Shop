from typing import Dict

class MenuItem:
    """Representa um item individual do menu (tamanho, proteína, adicional, etc.)."""

    def __init__(self, name: str, item_type: str, price: float) -> None:
        """Construtor da classe MenuItem."""
        pass

    def get_info(self) -> Dict[str, any]:
        """Retorna um dicionário com as informações do item."""
        pass

    def __str__(self) -> str:
        """Retorna uma representação em string do item."""
        pass

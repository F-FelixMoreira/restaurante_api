from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self) -> str:
        return self._nome

    def aplicar_desconto(self) -> None:
        self._preco -= (self._preco * 0.05)

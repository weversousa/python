# Agregação de Classes

*Exemplo*:
~~~python
from typing import Type


class Produto:

    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor

    def informacoes_produto(self) -> None:
        print(f'Produto: {self.nome} / valor: R$ {self.valor:.2f}')


class Carrinho:

    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        total = 0

        for produto in self.__produtos:
            produto.informacoes_produto()
            total += produto.valor

        print('Total: R$', total)
        self.__produtos.clear()


tv = Produto('TV LG', 1_350.99)
celular = Produto('Celular iPhone X', 3_600.70)
tinta = Produto('Cartucho impressora HP', 35)

carrinho = Carrinho()

carrinho.adicionar_produto(tv)
carrinho.adicionar_produto(celular)
carrinho.adicionar_produto(tinta)

carrinho.finalizar_compra()
~~~

*Saída*:
~~~python
Produto: TV LG / valor: R$ 1350.99
Produto: Celular iPhone X / valor: R$ 3600.70    
Produto: Cartucho impressora HP / valor: R$ 35.00
Total: R$ 4986.69
~~~
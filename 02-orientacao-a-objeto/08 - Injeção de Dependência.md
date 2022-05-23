# Injeção de Dependência

Injeção de dependência ocorre quando uma classe recebe como parãmetros a instância de outra classe em seu método construtor.

*Exemplo*:
~~~python
from typing import Type


class Casa:

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


class Pessoa:

    def __init__(self, nome: str, casa: Type[Casa]):
        self.__nome = nome
        self.__casa = casa

    def get_endereco(self):
        print(self.__casa.get_endereco())


casa = Casa('Av. Paulista, 200 - São Paulo/SP')
pessoa = Pessoa('Paula', casa)
pessoa.get_endereco()
~~~

*Saída*:
~~~python
Av. Paulista, 200 - São Paulo/SP
~~~
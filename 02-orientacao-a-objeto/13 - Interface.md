# Interface

É caracterizado uma interface quando todos os métodos de uma classe são abstratos.

*Exemplo*:
~~~python
from abc import ABC, abstractmethod
from typing import Type


class FormasInterface(ABC):

    @abstractmethod
    def get_perimetro(self) -> int:
        pass

    @abstractmethod
    def get_area(self) -> int:
        pass


class TerrenoQuadrado(FormasInterface):

    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_perimetro(self) -> int:
        return self.lado * 4

    def get_area(self) -> int:
        return self.lado * self.lado


class TerrenoRetangular(FormasInterface):

    def __init__(self, largura: int, comprimento: int) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self) -> int:
        return (self.comprimento * 2) + (self.largura * 2)

    def get_area(self) -> int:
        return self.largura * self.comprimento


class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu o perimetro: {terreno.get_perimetro()} m.')

    def medir_area(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu a área: {terreno.get_area()} m².')


engenehiro = Engenheiro('Marcos')

terreno_quadrado = TerrenoQuadrado(4)
terreno_retangular = TerrenoRetangular(2, 3)

engenehiro.medir_area(terreno_quadrado)
engenehiro.medir_perimetro(terreno_retangular)
~~~

*Saída*:
~~~python
Marcos mediu a área: 16 m².
Marcos mediu o perimetro: 10 m.
~~~
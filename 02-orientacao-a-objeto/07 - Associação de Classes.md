# Associação de Classes

*Exemplo*:
~~~python
from typing import Type


class Interruptor:
    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print(f'Acendendo a luz do {self.__comodo}')

    def apagar(self):
        print(f'Apagando a luz do {self.__comodo}')


class Pessoa:
    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


pessoa = Pessoa()
interruptor = Interruptor('Quarto')

# A associação, o objeto pessoa usará os métodos do obeto interruptor
pessoa.acender_luz(interruptor)
pessoa.apagar_luz(interruptor)

# Método do próprio objeto pessoa
pessoa.dormir()
~~~

*Saída*:
~~~python
Acendendo a luz do Quarto
Apagando a luz do Quarto

Fui dormir...
~~~
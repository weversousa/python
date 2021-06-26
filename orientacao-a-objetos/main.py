from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def modo_de_falar(self):
        ...


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def modo_de_falar(self):
        print(f'O {self.nome} LATE!')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def modo_de_falar(self):
        print(f'O {self.nome} MIA!')


animal1 = Cachorro('Scooby')
animal1.modo_de_falar()

animal2 = Gato('Garfield')
animal2.modo_de_falar()

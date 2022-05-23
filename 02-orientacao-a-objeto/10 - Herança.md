# Herança

* `self.__` Privado
* `self._` Protegido
* `self.` Público

|       | Privado (-) | Protegido (#)   | Público (+)
:-      | :-:         | :-:             | :-:
Classe  | X           | X               | X
Herança |             | X               | X
Objeto  |             | só em Python :( | X

*Exemplo*:
~~~python
class Avo:

    def __init__(self):
        self.__nome = 'Paulo'
        self._idade = 50
        self.sobrenome = 'Macedo'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


class Pai(Avo):

    def __init__(self):
        super().__init__()
        self.__nome = 'Pedro'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


class Filho(Pai):

    def __init__(self):
        super().__init__()
        self.__nome = 'Thiago'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


pai = Pai()
pai.exibir_nome()

# sobrenome vai estar disponível em todos herdeiros
avo = Avo()
avo.exibir_nome()

filho = Filho()
filho.exibir_nome()
~~~

*Saída*:
~~~python
Pedro Macedo
Paulo Macedo
Thiago Macedo
~~~
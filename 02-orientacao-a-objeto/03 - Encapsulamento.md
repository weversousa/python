# Encapsulamento

*Exemplo*:
~~~python
class Pessoa:
    def __init__(self, nome, cpf) -> None:
        # Atributo público
        self.nome = nome
        # atributo privado
        self.__cpf = cpf

    # Método privado, somente acessível na classe
    def __verificar_cpf(self):
        if self.__cpf == '1234':
            return True
        return False

    # Método público, acessível através da instância
    def cpf_existe(self):
        if self.__verificar_cpf():
            print('CPF válido!')
        else:
            print('CPF inválido!')


pessoa_1 = Pessoa('Maria', '1234')
pessoa_1.cpf_existe()

pessoa_2 = Pessoa('Carlos', '7777')
pessoa_2.cpf_existe()
~~~

*Saída*:
~~~python
CPF válido!
CPF inválido!
~~~

*Exemplo*:
~~~python
class Calculadora:

    # Somente esse método será acessível
    def calcular(self, op, n1, n2):
        if op == '+':
            return self.__adicionar(n1, n2)
        elif op == '-':
            return self.__subtrair(n1, n2)
        else:
            print('Operação inválida.')

    # Esses métodos não vão ser acessíveis
    def __adicionar(self, n1, n2):
        return n1 + n2

    def __subtrair(self, n1, n2):
        return n1 - n2
~~~
# Associação Bidirecional

*Exemplo*:
~~~python
class Casa:

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco
        self.__proprietario = None

    def get_endereco(self):
        print(self.__endereco)
    
    def get_proprietario(self):
        self.__proprietario.get_nome()

    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario


class Pessoa:

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__casa = None

    def get_nome(self):
        print(self.__nome)

    def get_endereco(self):
        self.__casa.get_endereco()

    def set_casa(self, casa: any):
        self.__casa = casa


casa = Casa('Av. Jabaquara, 1400 - São Paulo/SP')
pessoa = Pessoa('Henrique')

# A casa receberá um objeto pessoa e pessoa receberá um obejto casa
casa.set_proprietario(pessoa)
pessoa.set_casa(casa)

# Agora a casa tem acesso a pessoa associada e vice-versa
casa.get_proprietario()
pessoa.get_endereco()
~~~

*Saída*:
~~~python
Henrique
Av. Jabaquara, 1400 - São Paulo/SP
~~~
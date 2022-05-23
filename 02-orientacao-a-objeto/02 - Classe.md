# Classe

A classe é a representação de uma determinada coisa na vida real.
Para criar uma classe usamos a palavra reservada `class` e a escrita em `PascalCase`.

Sobre a classe:
* Pode ou não ter parâmetros

*Exemplo*:
~~~python
class Pessoa:

    # Método construtor, é invocado assim que criar uma instância
    def __init__(self, nome):
        # Atributo de Instância, cada objeto terá o seu valor
        self.nome = nome

    def exibir_nome(self):
        print(self.nome)


# Criando uma instância da classe Pessoa, tornando a variável pessoa_1 em um objeto
pessoa_1 = Pessoa('Paula')

# Usando um método público da classe Pessoa
pessoa_1.exibir_nome()
~~~

*Saída*:
~~~python
Paula
~~~
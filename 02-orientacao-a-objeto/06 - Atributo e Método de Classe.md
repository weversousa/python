# Atributo e Método de Classe

## Atributo estático

O atributo de classe é chamado assim devido ao valor dele ser o mesmo para todos os objetos derivados da mesma classe é um valor **estático**.  
Esse atributo fica FORA do método construtor `__init__`.

Já o atributo de instância ele é individual para cada objeto derivado de uma mesma classe é um valor **dinâmico**.  
Esse atributo fica DENTRO do método construtor `__init__`.

Vamos criar duas instâncias diferentes da mesma classe.  
Ambas vão ter o mesmo sobrenome.

*Exemplo*:
~~~python
class Pessoa:
    sobrenome = 'Sousa'

    def __init__(self, nome):
        self.nome = nome


maria = Pessoa('Maria')
fabio = Pessoa('Fábio')

print(maria.nome, maria.sobrenome)
print(fabio.nome, fabio.sobrenome)
~~~

*Saída*:
~~~python
Maria Sousa
Fábio Sousa
~~~

É possível alterar um atributo estático diretamente pela classe.  
Todos os objetos vão ter seus valores alterados, mesmo se eles já tiverem sido criados.

*Exemplo*:
~~~python
class Pessoa:
    sobrenome = 'Sousa'

    def __init__(self, nome):
        self.nome = nome


joao = Pessoa('João')
clara = Pessoa('Clara')

print(joao.nome, joao.sobrenome)
print(clara.nome, clara.sobrenome)

Pessoa.sobrenome = 'Andrade'

print(joao.nome, joao.sobrenome)
print(clara.nome, clara.sobrenome)
~~~

*Saída*:
~~~python
João Sousa
Clara Sousa

João Andrade
Clara Andrade
~~~

Também é possível alterar o valor estático através de um dos objetos criado, nesse caso somente o valor desse objeto vai ser alterado e daí por diante esse objeto só pode ser alterado individualmente, mesmo se alterar através da classe ele não vai ser alterado.

*Exemplo*:
~~~python
class Pessoa:
    sobrenome = 'Silva'

    def __init__(self, nome):
        self.nome = nome


jaqueline = Pessoa('Jaqueline')
paula = Pessoa('Paula')

print(jaqueline.nome, jaqueline.sobrenome)
print(paula.nome, paula.sobrenome)

jaqueline.sobrenome = 'Ferraz'

print(jaqueline.nome, jaqueline.sobrenome)
print(paula.nome, paula.sobrenome)

Pessoa.sobrenome = 'Buarque'

print(jaqueline.nome, jaqueline.sobrenome)
print(paula.nome, paula.sobrenome)
~~~

*Saída*:
~~~python
Jaqueline Silva
Paula Silva

Jaqueline Ferraz
Paula Silva

Jaqueline Ferraz
Paula Buarque
~~~

O decorador `@classmethod` permite acessar um atributo de classe dentro da classe o self não funciona com atributos de classe.

Dessa forma, mesmo alterando o atributo estático através de um dos objetos, agora todos os objetos vão ter o mesmo valor de atributo estático, o objeto tem controle sobre o contexto de classe.

*Exemplo*:
~~~python
class Pessoa:
    sobrenome = 'Sousa'

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def alterar_sobrenome(cls, novo_valor):
        cls.sobrenome = novo_valor


ronaldo = Pessoa('Ronaldo')
adriano = Pessoa('Adriano')
luiz = Pessoa('Luiz')

print(ronaldo.nome, ronaldo.sobrenome)
print(adriano.nome, adriano.sobrenome)
print(luiz.nome, luiz.sobrenome)

adriano.alterar_sobrenome('Ferreira')

print(ronaldo.nome, ronaldo.sobrenome)
print(adriano.nome, adriano.sobrenome)
print(luiz.nome, luiz.sobrenome)
~~~

*Saída*:
~~~python
Ronaldo Sousa
Adriano Sousa
Luiz Sousa

Ronaldo Ferreira
Adriano Ferreira
Luiz Ferreira
~~~

## Método estático

Não é possível interagir com a classe, não dá para usar self ou cls.  
Os métodos estáticos podem ser usados sem criar uma instância da classe.

*Exemplo*:
~~~python
class Saudacao:

    @staticmethod
    def exbir_mensagem():
        print('Salve galera!')


Saudacao.exbir_mensagem()
~~~

*Saída*:
~~~python
Salve galera!
~~~


*Exemplo*:
~~~python
~~~

*Saída*:
~~~python
~~~

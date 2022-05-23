# Função

A função é um bloco de códgo que executa uma funcionalidade específica, normalmente algo que vai se repetir no programa e para criar uma função usamos a palavra reservada `def` e a escrita em `snake_case`.

Sobre a função:
* Pode ou não ter retorno
* Pode ou não ter parâmetros

Para usar uma função existente é necessário escrever o nome da função com `()` na frente, sem a palavra `def`.

## Sem retorno

*Exemplo*:
~~~python
def saudacao():
    print('Bom dia!')


saudacao()
~~~

*Saída*:
~~~python
Bom dia!
~~~

## Com retorno e parâmetros

Nesse caso é obrigatório passar argumentos para função ao chamá-la devido aos seus parâmetros.

*Exemplo*:
~~~python
def somar(n1, n2):
    return n1 + n2


print(somar(2, 3))
~~~

*Saída*:
~~~python
5
~~~

## Parâmetro com valor padrão

Nesse caso não é obrigatório passar nada para função ao chamá-la.

*Exemplo*:
~~~python
def somar_um(p1=1, n2=1):
    return n1 + n2


print(somar_um())
~~~

*Saída*:
~~~python
2
~~~

## Parâmetros obrigatório e não obrigatório

Parâmetros sem valor padrão "obrigatoriamente" vem primeiro.
Nesse caso é obrigatório ao chamar a função, passar um argumento.

*Exemplo*:
~~~python
def somar_um(n1, n2=1):
    return n1 + n2


print(somar_um(3))
print(somar_um(6, 2))
~~~

*Saída*:
~~~python
4
8
~~~
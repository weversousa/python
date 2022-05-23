# Empacotamento

## Tupla

O caractere asterísco faz com que a variável args seja uma tupla.
Sendo assim poderá receber uma quantidade indeterminada de argumentos.

*Exemplo*:
~~~python
def funcao(*args):
    print(args)
    print(type(args))


funcao('a', 3, [3, 5], {'nome': 'Pedro'})
~~~

*Saída*:
~~~python
('a', 3, [3, 5], {'nome': 'Pedro'})
<class 'tuple'>
~~~

## Dicionário

Os caracteres asteríscos fazem com que a variável kwargs seja um dicionário.
Sendo assim poderá receber uma quantidade indeterminada de argumentos.

Como o paramêtro é um dicionário, é necessário passar os argumentos de forma nomeada (chave/valor).

*Exemplo*:
~~~python
def funcao(**kwargs):
    print(kwargs)
    print(type(kwargs))


funcao(nome='Neymar', idade=29, time='PSG')
~~~

*Saída*:
~~~python
{'nome': 'Neymar', 'idade': 29, 'time': 'PSG'}
<class 'dict'>
~~~

## Tupla e Dicionário

*Exemplo*:
~~~python
def funcao(*args, **kwargs):
    print(args)
    print(kwargs)


funcao('Brasil', 'Espanha', 'Itália', competicao='Copa do Mundo', ano=2022, pais_sede='Catar')
~~~

*Saída*:
~~~python
('Brasil', 'Espanha', 'Itália')
{'competicao': 'Copa do Mundo', 'ano': 2022, 'pais_sede': 'Catar'}
~~~
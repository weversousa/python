# Tupla

A estrutura de dados Tupla (tuple) é composta por qualquer sequência de elementos envolvidos entre `()` e separados por `,`.

Uma observação, caso tenha somente 1 elemento dentro dos `()` tem que colocar uma `,`, caso contrário não será uma tupla.

Também é possível criar uma Tupla sem os `()`, é só criar uma sequência de caracteres separados por `,` e seguir a observação acima, deve ter pelo menos uma `,`.

* indexada
* heterogênea
* imutável
* aceita repetição

*Exemplo*:
~~~python
cores = ('azul',)
print(cores)
print(type(cores))

cores = ('azul')
print(cores)
print(type(cores))
~~~

*Saída*:
~~~python
('azul',)
<class 'tuple'>

azul
<class 'str'>
~~~

*Exemplo*:
~~~python
frutas = 'maçã',
print(frutas)
print(type(frutas))

frutas = 'maçã'
print(frutas)
print(type(frutas))
~~~

*Saída*:
~~~python
('maçã',)
<class 'tuple'>

maçã
<class 'str'>
~~~

*Exemplo*:
~~~python
carros = ('uno', 'hb20')
print(carros)
print(type(carros))

marcas = 'fiat', 'honda'
print(marcas)
print(type(marcas))
~~~

*Saída*:
~~~python
('uno', 'hb20')
<class 'tuple'>

('fiat', 'honda')
<class 'tuple'>
~~~

Seguir exemplos da Lista para manipular a Tupla, menos as regras de mutação.
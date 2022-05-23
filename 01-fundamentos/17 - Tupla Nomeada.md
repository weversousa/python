# Tupla Nomeada

*Exemplo*:
~~~python
from collections import namedtuple


Estados = namedtuple(typename='Estados', field_names=['sigla', 'nome'])

estado_sp = Estados(sigla='SP', nome='São Paulo')
print(estado_sp)
print(estado_sp.sigla)
print(estado_sp.nome)

estado_ba = Estados('BA', 'Bahia')
print(estado_ba)
print(estado_ba.sigla)
print(estado_ba.nome)
~~~

*Saída*:
~~~python
Estados(sigla='SP', nome='São Paulo')
SP
São Paulo

Estados(sigla='BA', nome='Bahia')
BA
Bahia
~~~
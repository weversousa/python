# Biblioteca math

A biblioteca `math` não é nativa do Python porém já vem instalada junto ao Python e serve para se trabalhar com números. É necessário importá-la para uso.

Alguns de seus métodos importantes são:
* `ceil()` arredonda para o maior número inteiro mais próximo
* `floor()` arredonda para o menor número inteiro mais próximo
* `srqt()` raiz quadrada
* `pow()` exponenciação

*Exemplo*:
~~~python
from math import ceil, floor, sqrt, pow


print(ceil(9.9483020))
print(floor(9.9483020))
print(sqrt(49))
print(pow(2, 3))  # O mesmo que 2 ** 3. Escrita 2³
~~~

*Saída*:
~~~python
10
9
7.0
8.0
~~~
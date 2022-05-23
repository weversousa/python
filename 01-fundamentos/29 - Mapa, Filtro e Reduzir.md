## Mapa

A classe mapa (map) é nativa e pede dois parâmetros, uma função e um iterável. A função vai ser aplicada a cada item do iterável e vai devolver uma lista de mesmo tamanho do iterável original.

O retorno do método map é um objeto, e para usar os valor como lista é necessário converter com a classe `list`.


*Exemplo*:
~~~python
numeros = [1, 2, 3, 4, 5]
numeros_mais_um = list(map(lambda numero: numero + 1, numeros))
print(numeros_mais_um)
~~~

*Saída*:
~~~python
[2, 3, 4, 5, 6]
~~~

## Filtro

A classe filtro (filter) é nativa e pede dois parâmetros, uma função ou None e um iterável. A função vai ser aplicada a cada item do iterável e vai devolver uma lista somente com os valores verdadeiros.

*Exemplo*:
~~~python
numeros = [1, 2, 3, 4, 5]
numeros_pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print(numeros_pares)
~~~

*Saída*:
~~~python
[2, 4]
~~~

No caso abaixo vamos enviar None ao invés de uma função, sendo assim o filter vai devolver somente os valores que resultam em verdadeiro, a gente já viu isso em tipo lógico.

*Exemplo*:
~~~python
dados = [0, 1, 2, 3, '', ' ', True, False]
verdadeiros = list(filter(None, dados))
print(verdadeiros)
~~~

*Saída*:
~~~python
[1, 2, 3, ' ', True]
~~~

## Reduzir

O método `reduce` não é nativo e por isso é necessário importar da biblioteca `functools` que já vem instalada com o Python.

O método `reduce` retorna um único valor, que vai depender da lógica da sua função.
Esse método espera por 3 parâmetros, uma função, um iterável e um valor inicial, sendo o último não obrigatório.

Caso não passado o valor inicial ele vai usar o primeiro valor do iterável.

*Exemplo*:
~~~python
from functools import reduce


def somar(esquera, direita):
    print(esquera, direita)
    return esquera + direita


print(reduce(somar, [1, 2, 3, 4, 5], 0))
print(reduce(somar, [1, 2, 3, 4, 5]))
~~~

*Saída*:
~~~python
0 1  # o 0 é o valor incial e o 1 é o primeiro valor da lista
1 2  # o 1 é soma da linha acima e o 2 é o próximo valor da lista
3 3  # o 3 é soma da linha acima e o outro 3 é o próximo valor da lista
6 4  # o 6 é soma da linha acima e o outro 4 é o próximo valor da lista
10 5  # o 10 é soma da linha acima e o outro 5 é o próximo valor da lista
15  # esse é a soma da linha acima e o fim da execução pois a lista terminou

1 2
3 3
6 4
10 5
15
~~~

*Exemplo*:
~~~python
from functools import reduce


def e_maior(inicial, proximo):
    print(inicial, proximo)

    if proximo > inicial:
        return proximo
    else:
        return inicial


print(reduce(e_maior, [11, 2, 33, 0, 9]))
~~~

*Saída*:
~~~python
11 2
11 33
33 0
33 9
33
~~~

O método `print` dentro das funções exibindo os dois valores é para ilustração, isso não é feito e também normalmente ao usar `map`, `reduce` e `filter` é usado uma função `lambda`.

O exemplo abaixo faz o mesmo que o exemplo acima e com bem menos linhas de código.

*Exemplo*:
~~~python
from functools import reduce


maior_numero = reduce(lambda x, y: x if x > y else y, [11, 2, 33, 0, 9])
print(maior_numero)
~~~

*Saída*:
~~~python
33
~~~
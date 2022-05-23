# Lista

A estrutura de dados Lista (list) é composta por qualquer sequência de elementos envolvidos entre `'[]` e separados por `,`.

Sobre a Lista:
* classe
* indexada
* heterogênea
* mutável
* aceita repetição

*Exemplo*:
~~~python
frutas = ['uva', 'pêra', 'cajú']

print(type(frutas))
print(frutas)
~~~

*Saída*:
~~~python
<class 'list'>
['uva', 'pêra', 'cajú']
~~~

## Indexação

Os elementos de uma lista podem ser acessados através de seu índice, com isso podemos pegar, alterar e deletar um valor pelo seu índice.

*Exemplo*:
~~~python
frutas = ['uva', 'pêra', 'cajú']

print(frutas[0])
print(frutas[1])
print(frutas[2])

frutas[2] = 'melão'
print(frutas)

del frutas[1]
print(frutas)
~~~

*Saída*:
~~~python
uva
pêra
cajú

['uva', 'pêra', 'cajú']

['uva', 'cajú']
~~~

## Classe list

A classe `list` é uma classe nativa e através dela é possível converter qualquer iterável em lista. E por ser uma classe possui métodos para trabalhar com seus elementos.

Vimos mais acima como criar uma lista de forma literal usando `[]` que a forma mais usada, porém abaixo um exemplo de como criar uma lista através da classe `list`, que vai receber uma **string** que já vimos ser um iterável, poderia ser uma tupla, dicionário ou conjunto.

*Exemplo*:
~~~python
vogais = list('aeiou')

print(type(vogais))
print(vogais)
~~~

*Saída*:
~~~python

<class 'list'>
['a', 'e', 'i', 'o', 'u']
~~~

### Função index

O método `index` pertence à classe list e retorna o índice de um elemento da lista através do seu nome.

*Exemplo*:
~~~python
frutas = ['uva', 'pêra', 'cajú']
print(frutas.index('cajú'))
~~~

*Saída*:
~~~python
2
~~~

### Função pop

O método `pop` pertence à classe list e remove um elemento da lista através do seu índice, esse método também retorna o valor deletado.

Se não passado o índice do eleento a ser deletado por padrão o método remove o útlimo elemento da lista.

*Exemplo*:
~~~python
uf = ['sp', 'ba', 'mg', 'rj']

uf_deletado = uf.pop()
print(uf_deletado)
print(uf)

uf_deletado = uf.pop(0)
print(uf_deletado)
print(uf)
~~~

*Saída*:
~~~python
rj
['sp', 'ba', 'mg']

sp
['ba', 'mg']
~~~

### Função remove

O método `remove` pertence à classe list e exclui um elemento da lista através do seu nome. Caso o nome não exista acontece uma excessão.

*Exemplo*:
~~~python
casa = ['porta', 'janela', 'telhado']

casa.remove('janela')
print(casa)

casa.remove('chaminé')
~~~

*Saída*:
~~~python
['porta', 'telhado']

KeyError
~~~

### Função sort

O método `sort` pertence à classe list e ordena a lista por ordem alfabética.

Por padrão a lista é ordenada em ordem crescente, para ordenar em ordem decrescente passar o parâmetros `reverse=True`.

*Exemplo*:
~~~python
vogais = ['i', 'u', 'a', 'e', 'o']

vogais.sort()
print(vogais)

vogais.sort(reverse=True)
print(vogais)
~~~

*Saída*:
~~~python
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
~~~

### Função reverse

O método `reverse` pertence à classe list e inverte ordem dos elementos de trás para a frente.

*Exemplo*:
~~~python
nomes = ['Ana', 'Bia', 'Caio', 'Téo']

nomes.reverse()
print(nomes)
~~~

*Saída*:
~~~python
['Téo', 'Caio', 'Bia', 'Ana']
~~~

### Função append

O método `append` pertence à classe list e adiciona um novo elemento ao final da lista.

*Exemplo*:
~~~python
cores = ['azul', 'verde']

cores.append('branca')
print(cores)
~~~

*Saída*:
~~~python
['azul', 'verde', 'branca']
~~~

### Função insert

O método `insert` pertence à classe list e adiciona um novo elemento a lista no ídice informado, caso já tenha um elemento no mesmo índice, ele pega o lugar desse elemento e faz com que o elemento que estava ali e todos os demais a direita na lista passem para um ídice a frente.


*Saída*:
~~~python
cidades = ['Osasco', 'Salvador']

cidades.insert(0, 'Serrinha')
print(cidades)
~~~

*Saída*:
~~~python
['Serrinha', 'Osasco', 'Salvador']
~~~

### Função count

O método `count` pertence à classe list e retorna a quantidade de vezes que um elemento se repete na lista.

*Exemplo*:
~~~python
estados = ['ativo', 'desativado', 'pendente', 'ativo', 'ativo']
print(estados.count('ativo'))
~~~

*Saída*:
~~~python
3
~~~

## Função len

O método `len` é nativo e retorna o tamanho da lista (quantidade de elementos).

*Exemplo*:
~~~python
carros = ['fusca', 'gol', 'uno', 'tempra']
print(len(carros))
~~~

*Saída*:
~~~python
4
~~~

## Matriz

Cada lista interna é 1 elemento da lista externa Matriz, a função nativa `len` por exemplo vai contar cada lista interna como 1 elemento para definir o tamanho da matriz, independente da quantidade de elementos que tenha a lista interna.

*Exemplo*:
~~~python
matriz = [
    ['arroz', 'feijão', 'café'],
    [24.90, 9.83, 16.50]
]

print('Prosuto:', matriz[0][0], '|', 'Preço:', matriz[1][0])
print('Prosuto:', matriz[0][1], '|', 'Preço:', matriz[1][1])
print('Prosuto:', matriz[0][2], '|', 'Preço:', matriz[1][2])

print(len(matriz))
print(len(matriz[0]))
print(len(matriz[1]))
~~~

*Saída*:
~~~python
Prosuto: arroz | Preço: 24.9
Prosuto: feijão | Preço: 9.83
Prosuto: café | Preço: 16.5

2
3
3
~~~

## Heterogênea

A estrutura de dados lista aceita criar uma lista com tipos diferentes de dados.

*Exemplo*:
~~~python
homogenea = [1, '2', 15.85, True, False, ['uva'], ('azul'), {'nome': 'Paula'}]
~~~

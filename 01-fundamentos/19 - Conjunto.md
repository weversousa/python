# Conjunto

A estrutura de dados Conjunto (set) é composta por qualquer sequência de elementos envolvidos entre `'{}` e separados por `,`.

Sobre a Dicionário:
* classe
* não indexada
* heterogênea
* mutável
* não aceita repetição

Criando um dicionário de forma Literal, onde os valores são definidos no momento de sua criação.

*Exemplo*:
~~~python
vogais = {'a', 'e', 'e', 'a', 'i', 'o', 'a', 'i', 'u', 'u'}

print(type(vogais))
print(vogais)
~~~

*Saída*:
~~~python
<class 'set'>
{'u', 'e', 'a', 'i', 'o'}
~~~

## Classe set

A classe `set` é uma classe nativa e através dela é possível criar um conjunto. E por ser uma classe possui métodos para trabalhar com seus elementos.

Vimos mais acima como criar um conjunto de forma literal usando `{}` que a forma mais usada, porém abaixo um exemplo de como criar um conjunto através da classe `set` que recebe como parâmetro um iterável.

*Exemplo*:
~~~python
frutas = set(['banana', 'maçã', 'banana', 'uva', 'banana', 'maçã', 'uva',])
print(type(frutas))
print(frutas)

vogais = set('aeioouu')
print(type(vogais))
print(vogais)
~~~

*Saída*:
~~~python
<class 'set'>
{'uva', 'banana', 'maçã'}

<class 'set'>
{'u', 'e', 'a', 'i', 'o'}
~~~

### Função add

O método `add` pertence à classe set e adiciona um novo elemento.

*Exemplo*:
~~~python
nomes = set()
nomes.add('Mary')
nomes.add('Pedro')
nomes.add('Pedro')

print(nomes)
~~~

*Saída*:
~~~python
{'Pedro', 'Mary'}
~~~

### Função remove

O método `remove` pertence à classe set e exclui um elemento do Conjunto através do seu nome. Caso o nome não exista acontece uma excessão.

*Exemplo*:
~~~python
numeros = set(['1', '2', '3'])

numeros.remove('2')
print(numeros)

numeros.remove('7')
~~~

*Saída*:
~~~python
{'3', '1'}

KeyError
~~~

### Função discard

O método `discard` pertence à classe set e exclui um elemento do Conjunto através do seu nome. Mas nesse caso se o nome não existir **não** acontece uma excessão.


*Exemplo*:
~~~python
letras = set(['a', 'b', 'c'])

letras.discard('c')
print(letras)

letras.discard('j')
print(letras)
~~~

*Saída*:
~~~python
{'a', 'b'}

{'a', 'b'}
~~~

### Função clear

O método `clear` pertence à classe set e exclui **todos** os elementos do Conjunto.

*Exemplo*:
~~~python
cores = set(['azul', 'verde', 'preto', 'verde'])

cores.clear()
print(cores)
~~~

*Saída*:
~~~python
set()
~~~

## Operação Matemática

### A ∪ B

É o mesmo que A união com B.

*Exemplo*:
~~~python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}

print(A.union(B))
print(A | B)
~~~

*Saída*:
~~~python
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
~~~

### A ∩ B

É o mesmo que A interseção com B (elementos que aparecem em ambos).

*Exemplo*:
~~~python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8, 9}

print(A.intersection(B))
print(A & B)
~~~

*Saída*:
~~~python
{0, 9}
{0, 9}
~~~

### A \ B

É o mesmo que A diferente de B.

*Exemplo*:
~~~python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8, 9}

print(A.difference(B))
print(A - B)
~~~

*Saída*:
~~~python
{1, 3, 5, 7}
{1, 3, 5, 7}
~~~

Símbolo Matemático | Operador Python | Descrição
:---:              | :---:           | ---
E ∈ S              | in              | elemento E é membro de S
A ⊆ B              | <=              | A é um subconjunto de B
A ⊂ B              | <               | A é um subconjunto próprio de B
A ∪ B              | \|              | A união com B
A ∩ B              | &               | A interseção com B
A ∖ B              | -               | diferença entre A e B
# Desempacotamento

## Desembrulhando Tupla e Lista

*Exemplo*:
~~~python

nome, idade, cor = ['Weverton', 31, 'preta']
print(nome, idade, cor)

nome, idade, cor = ('Weverton', 31, 'preta')
print(nome, idade, cor)
~~~

*Saída*:
~~~python
'Weverton', 31, 'preta'
'Weverton', 31, 'preta'
~~~

É necessário que a quantidade de variáveis sejam iguais a quantidade de valores da estrutura, do contrário é gerado uma excessão.

Abaixo um exemplo onde estamos declarando 4 variáveis para uma estrutura com 3 valores.

*Exemplo*:
~~~python
nome, idade, cor, sexo = ['Weverton', 31, 'preta']
~~~

*Saída*:
~~~python
ValueError: not enough values to unpack (expected 4, got 3)
~~~

Abaixo um exemplo onde estamos declarando 3 variáveis para uma estrutura com 4 valores.

*Exemplo*:
~~~python
nome, idade, cor = ['Weverton', 31, 'preta', 'masculino']
~~~

*Saída*:
~~~python
ValueError: too many values to unpack (expected 3)
~~~

### A expressão estrelada

Podemos usar a expressão estrelada `*variavel` para desembrulhar litas e tuplas.
Conforme exemplos acima se não passarmos a quantidade de variáveis corretas teremos uma excessão.
Mas vamos supor que a gente queira extrair os primeiros ou os últimos ou ambos itens da estrutura.

A variável com `*` vai se tornar uma lista, contendo os demais valores não extraídos.

*Exemplo*:
~~~python
nome, idade, cor, *restante = ('Weverton', 31, 'preta', 'masculino', 1.65)
print(nome, idade, cor)
print(restante)

*restante, sexo, altura = ['Weverton', 31, 'preta', 'masculino', 1.65]
print(sexo, altura)
print(restante)

nome, *restante, altura = ['Weverton', 31, 'preta', 'masculino', 1.65]
print(nome, altura)
print(restante)
~~~

*Saída*:
~~~python
Weverton 31 preta
['masculino', 1.65]

masculino 1.65
['Weverton', 31, 'preta']

Weverton 1.65
[31, 'preta', 'masculino']
~~~

Com o `_` podemos ignorar valores, na verdade os valores não são ignorados, pois eles são armazenados no `_`, podemos dizer que uma convenção para valores que não vão ser usados.

*Exemplo*:
~~~python
x, _, y = [1, 2, 3]
print(x, y)

x, y, *_ = [1, 2, 3, 4, 5]
print(x, y)
~~~

*Saída*:
~~~python
1 3
~~~

Nesse caso abaixo o `*` está retirando todos os valores da estrutura.
Somente aplicável para funções.

*Exemplo*:
~~~python
def funcao(param_1, param_2, param_3):
    print(param_1, param_2, param_3)


funcao(*('Paula', 'João', 'Hélio'))
funcao(*['Paula', 'João', 'Hélio'])
funcao(*{'Paula', 'João', 'Hélio'})
~~~

*Saída*:
~~~python
Paula João Hélio
Paula João Hélio
Paula João Hélio
~~~

## Desembrulhando Dicionário

*Exemplo*:
~~~python
def funcao(nome, idade):
    print(nome, idade)


funcao(**{'nome': 'Leandro', 'idade': 30})
~~~

*Saída*:
~~~python
Leandro 30
~~~
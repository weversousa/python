# Python Fundamentos


## Comentário
```python
# Comentário de uma linha

"""
Comentário de
múltiplas linhas
com aspas duplas
"""

'''
Comentário de
múltiplas linhas
com aspas simples
'''
```


## Variável
```python
# snake_case
primeiro_nome
sobrenome
ultimo_nome
```


## Constante
```python
# letras maiúsculas
PI
URL_DATABASE
```


## String
* uma sequência de caracteres
* imutável
* indexada

```python
print(type('Paula'))
print(type("João"))

saída:
<class 'str'>
<class 'str'>

```

```python
print('uva'.upper())

saída: UVA
```

```python
print('AZUL'.lower())

saída: azul
```

```python
print('carlos'.capitalize())

saída: Carlos
```

```python
# Retorna o índice que inicia a palavra
print('bom dia'.find('dia'))

saída: 4
```

```python
# Retorna o índice exato do caractere
print('Ana'.find('n'))

saída: 1
```

```python
# Transforma a String em uma lista
# caso não passado parâmetro usa o espaço para separar
print('maçã mamão melão'.split())

saída: ['maçã', 'mamão', 'melão']
```

```python
print('arroz;macarrão;leite'.split(';'))

saída: ['arroz', 'macarrão', 'leite']
```

```python
print('Minha cor favorita é azul'.replace('azul', 'vermelha'))

saída: Minha cor favorita é vermelha
```

```python
# Acessar valores da String através do índice
print('AEIOU'[0])
print('AEIOU'[1])
print('AEIOU'[2])
print('AEIOU'[3])
print('AEIOU'[4])

saída:
A
E
I
O
U
```

```python
# Concatenação simples
cidade = 'Osasco'
uf = 'SP'
print(cidade + '/' + 'uf')

saída: Osasco/SP
```

```python
# Concatenação através do método "format"
cidade = 'Osasco'
uf = 'SP'
print('{}/{}'.format(cidade, uf))

saída: Osasco/SP
```

```python
# Concatenação através do "fstring"
cidade = 'Osasco'
uf = 'SP'
print(f'{cidade}/{uf}')

saída: Osasco/SP
```

```python
print('!' * 3)

saída: !!!
```

```python
# Tamanho da String, espaço incluso
print(len('Ana Maria'))

saída: 9
```


## Int
```python
print(type(7))
print(type('11'))
print(type(int('11')))
print(type(int('a11')))

saída:
<class 'int'>
<class 'str'>
<class 'int'>
ValueError
```


## Float
```python
print(type(3.9))
print(type('7.5'))
print(type(float('7.5')))
print(type(float('cf7.5')))

saída:
<class 'float'>
<class 'str'>
<class 'float'>
ValueError
```

```python
print(round(1.2837382038, 2))
print(round(1.2837382038, 1))
print(round(1.6))
print(round(1.4))
print(round(1.5))

saída:
1.28
1.3
2
1
2
```

### Biblioteca MATH
```python
from math import ceil, floor, sqrt, pow
# Maior número mais próximo
print(ceil(9.9483020))
# Menor número mais próximo
print(floor(9.9483020))
# Raiz quadrada
print(sqrt(49))
# Exponenciação
print(pow(2, 3))

saída:
10
9
7.0
8.0
```

### Formatação numérica com FSTRING
```python
print(f'{9.8268:.2f}')
print(f'{9.8268:.1f}')

saída:
9.83
9.8
```

```python
# Determinar um tamanho fixo de números
print(f'{1:0>10}')
print(f'{3:0<10}')
print(f'{77:0^10}')
print(f'{4:0>10.3f}')

saída:
0000000001
3000000000
0000770000
000004.000
```

```python
# Determinar um tamanho fixo de caracteres (exemplo de uso: alinhar saída)
fruta_1, fruta_2, fruta_3 = 'Banaba', 'Maça', 'Uva'
print(f'{fruta_1: <10} R$ 2,50')
print(f'{fruta_2: <10} R$ 5,50')
print(f'{fruta_3: <10} R$ 7,50')

saída:
12345678910 => 10 caracteres até começar o valor, deixando todos o valores alinhados
Banaba     R$ 2,50
Maça       R$ 5,50
Uva        R$ 7,50
```


## Boolean
```python
print(type(True))
print(type(False))

saída:
<class 'bool'>
<class 'bool'>
```

```python
# Valores False
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))

# Valores True
print(bool(1))
print(bool(' '))
print(bool('a'))
print(bool(['ovo']))
print(bool(('arros', 'manteiga')))
print(bool({'nome': 'Maria'}))

saída:
False
False
False
False
False
False

True
True
True
True
True
True
```

```python
# Também podemos obter o memso resultado acima usando a dupla negação de uma valor
print(not not 0)
print(not not 1)

saída:
False
True
```


# None
```python
# É o mesmo que NULL em outras linguagens
print(type(None))

saída: <class 'NoneType'>
```

```python
nome = 'Paula'
if nome:
    print(nome)
else:
    print('Valor Nulo')

saída: Paula
```

```python
nome = None
if nome:
    print(nome)
else:
    print('Valor Nulo')

saída: Valor Nulo
```

### Deletar uma variável
```python
nome = 'Clara'
del nome
print(nome)

saída: NameError
```


## Coerção automática
```python
# Signifa que o Python é de tipagem dinâmica
# Uma variável pode receber valor de qualquer tipo
x = 3
print(type(x))

x = 'Paula'
print(type(x))

x = True
print(type(x))

x = ['a', 'e']
print(type(x))

saída:
<class 'int'>
<class 'str'>
<class 'bool'>
<class 'list'>
```


## I/O
```python
# I input
x = input('Digite um número: ')

# O output
print(x)
```

```python
# Pegar argumentos digitados no terminal ao executar um arquivo Python
from sys import argv

if __name__ == '__main__':
    print(argv)

# Executar no terminal
python <nome_arquivo.py> oi este é um teste

saída:
['.\\obter_argumento_do_terminal.py', 'oi', 'este', 'é', 'um', 'teste']
```


## Operador Atribuição

### Simples
```python
fruta = 'banana'
nota = 10.0
```

### Composta
```python
n = 6

n += 2
n -= 4
n *= 6
n /= 2
n %= 5
```

### Múltipla
```python
nome, idade = 'Weverton', 30
```


## Operador Relacional
```python
print(5 > 3)
print(5 < 3)
print(6 == 8)
print(10 >= 5)
print(10 <= 5)

saída:
True
False
False
True 
False
```


## Operador Lógico
```python
# E
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# OU
print(True or True)
print(True or False)
print(False or True)
print(False or False)

saída:
True
False
False
False

True
True
True
False
```


## Operador de Negação
```python
print(not True)
print(not not False)

print(not False)
print(not not True)

saída:
False
False

True
True
```


## Lista
* indexada
* heterogênea
* mutável
* aceita repetição

```python
frutas = ['uva', 'pêra', 'cajú']
print(type(frutas))

saída: <class 'list'>
```

```python
frutas = ['uva', 'pêra', 'cajú']
print(frutas[0])
print(frutas[1])
print(frutas[2])

saída:
uva
pêra
cajú
```

```python
frutas = ['uva', 'pêra', 'cajú']
del frutas[0]
print(frutas)

saída: ['pêra', 'cajú']
```

```python
uf = ['sp', 'ba', 'rj']
# O método pop retorna o valor deletado
print(frutas.pop())
print(uf)

saída:
rj
['sp', 'ba']
```

```python
uf = ['sp', 'ba', 'rj']
print(frutas.pop(0))
print(uf)

saída:
sp
['ba', 'rj']
```

```python
casa = ['porta', 'janela', 'telhado']
casa.remove('janela')
print(casa)

saída: ['porta', 'telhado']
```

```python
vogais = ['i', 'u', 'a', 'e', 'o']
vogais.sort()
print(vogais)

saída: ['a', 'e', 'i', 'o', 'u']
```

```python
vogais = ['i', 'u', 'a', 'e', 'o']
vogais.sort(reverse=True)
print(vogais)

saída: ['u', 'o', 'i', 'e', 'a']
```

```python
nomes = ['Ana', 'Bia', 'Caio', 'Téo']
nomes.reverse()
print(nomes)

saída: ['Téo', 'Caio', 'Bia', 'Ana']
```

```python
cores = ['azul', 'verde']
cores.append('branca')
print(cores)

saída: ['azul', 'verde', 'branca']
```

```python
estados = ['ativo', 'desativado', 'pendente', 'ativo', 'ativo']
print(estados.count('ativo'))

saída: 3
```

```python
frutas = ['uva', 'pêra', 'cajú']
print(frutas.index('cajú'))

saída: 2
```

```python
cidades = ['Osasco', 'Salvador']
cidades.insert(0, 'Serrinha')
print(cidades)

saída: ['Serrinha', 'Osasco', 'Salvador']
```

```python
matriz = [
    ['São Paulo', 'Rio de Janeiro', 'Salvador'],
    ['Cenoura', 'Abacaxi', 'Uva']
]
print(len(matriz))
print(matriz[0])
print(matriz[1])
print(matriz[0][2])
print(matriz[1][1])

saída:
2
['São Paulo', 'Rio de Janeiro', 'Salvador']
['Cenoura', 'Abacaxi', 'Uva']
Salvador
Abacaxi
```

```python
homogenea = [1, '2', 15.85, True, False, ['uva'], ('azul'), {'nome': 'Paula'}]
```


## Tupla
* indexada
* heterogênea
* imutável
* aceita repetição

```python
x = 1,
print(type(x))
print(x)

y = (1,)
print(type(y))
print(y)

vogais = tuple('aeiou')
print(type(vogais))
print(vogais)

# Caso só tenha um elemnto e não seja colocado vírgula, não será uma Tupla
x = 1
y = (1)
print(type(n))
print(type(y))

saída:
<class 'tuple'>
(1,)

<class 'tuple'>
(1,)

<class 'tuple'>
('a', 'e', 'i', 'o', 'u')

saída: <class 'int'>
saída: <class 'int'>
```

```python
# Tupla Nomeada
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

saída:
Estados(sigla='SP', nome='São Paulo')
SP
São Paulo

Estados(sigla='BA', nome='Bahia')
BA
Bahia
```


## Dicionário
```python
endereco = {'cep': '05110-030', 'numero': '1235'}
print(endereco)
print(type(endereco))

mercado = dict([('arroz', 22.40), ('feijão', 9.32), ('café', 13.50)])
print(mercado)
print(type(mercado))

pessoa = {}
pessoa['nome'] = 'Paula'
pessoa['sexo'] = 'feminino'
pessoa['idade'] = 'masculino'
print(pessoa)
print(type(pessoa))


saída:
{'cep': '05110-030', 'numero': '1235'}
<class 'dict'>

{'arroz': 22.4, 'feijão': 9.32, 'café': 13.5}
<class 'dict'>

{'nome': 'Paula', 'sexo': 'feminino', 'idade': 'masculino'}
<class 'dict'>
```

```python
estados = {'SP': 'Osasco', 'RJ': 'Ipanema'}
novos_estados = {'BA': 'Serrinha'}
estados.update(novos_estados)
print(estados)

saída: {'SP': 'Osasco', 'RJ': 'Ipanema', 'BA': 'Serrinha'}
```

```python
endereco = {
    'logradouro': 'Avenida Paulista',
    'numero': '1235',
    'bairro': 'Consolação'
}
print(endereco.keys())
print(endereco.values())

saída:
dict_keys(['logradouro', 'numero', 'bairro'])
dict_values(['Avenida Paulista', '1235', 'Consolação'])
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
print(produtos.get('cafe', 'Chave não encontrada.'))
print(produtos.get('nescau', 'Chave não encontrada.'))

saída:
9.9
Chave não encontrada.
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
print(produtos['cafe'])
print(produtos['nescau'])

saída
9.9
KeyError
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
print('leite' in produtos)
print('banana' in produtos)

saída:
True
False
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
print(3.40 in produtos.values())
print(100.00 in produtos.values())

saída:
True
False
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
print(produtos.pop('tomate', 'Chave não encontrada.'))
print(produtos.pop('açucar', 'Chave não encontrada.'))
print(produtos)

saída:
2.89
Chave não encontrada.
{'arroz': 28.9, 'cafe': 9.9, 'shampoo': 12.99, 'leite': 3.4}
```

```python
produtos = {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
del produtos['cafe']
print(produtos)
del produtos['açucar']

saída:
{'arroz': 28.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
KeyError
```

```python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

# Retorna uma lista com as "chaves" em ordem crescente
print(sorted(letras.keys()))

# Retorna uma lista com as "chaves" em ordem decrescente
print(sorted(letras.keys(), reverse=True))

saída:
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
```

```python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

# Retorna uma lista com os "valores" em ordem crescente
print(sorted(letras.values()))

# Retorna uma lista com os "valores" em ordem decrescente
print(sorted(letras.values(), reverse=True))

saída:
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
```

```python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

# Retorna uma lista de "tuplas, chave/valor" em ordem crescente (pela chave)
print(sorted(letras.items()))

# Retorna uma lista de "tuplas, chave/valor" em ordem decrescente (pela chave)
print(sorted(letras.items(), reverse=True))

saída:
[('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
[('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]
```

```python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

# Para obter um retorno igual acima, porém ordenado pelo "valor"
# é necessário usar o parâmetro key do sorted()
# e passar uma função que informará por qual índice da tupla será a ordenação
# a tupla é (chave "índice 0", valor "índice 1")

# Retorna uma lista de "tuplas, chave/valor" em ordem crescente (pelo valor)
print(sorted(letras.items(), key=lambda x: x[1]))

# Retorna uma lista de "tuplas, chave/valor" em ordem decrescente (pelo valor)
print(sorted(letras.items(), reverse=True, key=lambda item: item[1]))

saída:
[('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
[('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]
```

```python
letras = {'e': 2, 'u': 5, 'a': 1, 'o': 4, 'i': 3}

# Para "todos" os casos que o retorno é uma lista de tuplas com chave e valor
# é só usar o método dict para transformar em dicionário novamente
print(dict(sorted(letras.items(), reverse=True, key=lambda x: x[1])))

saída:
{'u': 5, 'o': 4, 'i': 3, 'e': 2, 'a': 1}
```


# Conjunto
* não aceita valores repetidos
  
```python
set_vogais = {'a', 'e', 'e', 'a', 'i', 'o', 'a', 'i', 'u', 'u'}
print(type(set_vogais))
print(set_vogais)

set_frutas = set(['banana', 'maça', 'banana', 'uva', 'banana', 'maça', 'uva', 'pêra'])
print(type(set_frutas))
print(set_frutas)

saída:
<class 'set'>
{'u', 'e', 'a', 'i', 'o'}

<class 'set'>
{'uva', 'banana', 'maça', 'pêra'}
```

```python
set_nomes = set()
set_nomes.add('Mary')
set_nomes.add('Pedro')
set_nomes.add('Pedro')
print(set_nomes)

saída:
{'Pedro', 'Mary'}
```

```python
numeros = set(['1', '2', '3'])
numeros.remove('2')
print(numeros)
numeros.remove('7')

saída:
{'3', '1'}
KeyError
```

```python
letras = set(['a', 'b', 'c'])
letras.discard('c')
print(letras)
# Não lança erro mesmo se não existir
letras.discard('j')

saída:
{'a', 'b'}
```

```python
cores = set(['azul', 'verde', 'preto', 'verde'])
cores.clear()
print(cores)

saída:
set()
```

### Operação Matemática
```python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}

# A ∪ B é o mesmo que A união com B
print(A.union(B))
print(A | B)

saída:
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

```python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8, 9}

# A & B é o mesmo que A interseção com B (elementos que aparecem em ambos)
print(A.intersection(B))
print(A & C)

saída:
{0, 9}
{0, 9}
```

Símbolo Matemático | Operador Python | Descrição
:---: | :---: | ---
E ∈ S | in | elemento E é membro de S
A ⊆ B | <= | A é um subconjunto de B
A ⊂ B | < | A é um subconjunto próprio de B
A ∪ B | \| | A união com B
A ∩ B | & | A interseção com B
A ∖ B | - | diferença entre A e B


# Built-in
```python
# Retorna sempre o valor como positivo
print(abs(-4))

# Retorna True se todos forem Verdadeiros
# Somente funciona em Iterável
print(all([1, ' ']))
print(all([0, '', True]))

saída:
4

True
False
```


## Função
```python
# Sem parâmetro e sem retorno
def saudacao():
    print('Bom dia!')

saudacao()

saída:
Bom dia!
```

```python
# Com parâmetro e retorno
def somar(number_1, number_2):
    return number_1 + number_2

# É obrigatório passar argumentos para atender os parâmetros
print(somar(2, 3))

saída:
5
```

```python
# Parâmetro com valor padrão
def somar_um(parametro_um=1, parametro_dois=1):
    return parametro_um + parametro_dois

# Não é obrigatório passar argumentos
print(somar_um())

saída:
2
```

```python
# Parâmetros sem valor padrão "obrigatoriamente" vem primeiro
def somar_um(parametro_um, parametro_dois=1):
    return parametro_um + parametro_dois

# Nesse caso é obrigatório ao chamar a função, passar um argumento
print(somar_um(3))
print(somar_um(6, 2))

saída:
4
8
```

### Recursividade
```python
# Uma função recursiva, chama a si até o parâmetro atingir a condição desejada
def funcao(numero):
    if numero > 5:
        print('Encerrado!!!!!')
    else:
        print(f'O numero está valendo {numero}')
        return funcao(numero + 1)

funcao(1)

saída:
O numero está valendo 1
O numero está valendo 2
O numero está valendo 3
O numero está valendo 4
O numero está valendo 5
Encerrado!!!!!
```

### Decorador
```python
def funcao_decorador(minha_funcao):

    def wrapper(nome):
        print('===== Cabeçalho =====')
        minha_funcao(nome)
        print('===== Rodapé =====')

    return wrapper


@funcao_decorador
def exibr_nome(nome):
    print(f'Olá senhor (a) {nome}.')


exibr_nome('Jaqueline')

saída:
===== Cabeçalho =====
Olá senhor (a) Jaqueline.
===== Rodapé =====
```

### Empacotamento
```python
# O caractere asterísco faz com que a variável args seja uma tupla
# Sendo assim poderá receber uma quantidade indeterminada de argumentos
def funcao(*args):
    print(args)
    print(type(args))

funcao('a', 3, [3, 5], {'nome': 'Pedro'})

saída:
('a', 3, [3, 5], {'nome': 'Pedro'})
<class 'tuple'>
```

```python
# Os caracteres asteríscos fazem com que a variável kwargs seja um dicionário
# Sendo assim poderá receber uma quantidade indeterminada de argumentos
def funcao(**kwargs):
    print(kwargs)
    print(type(kwargs))

# Como o paramêtro é um dicionário
# É necessário passar os argumentos de forma nomeada (chave/valor)
funcao(nome='Neymar', idade=29, time='PSG')

saída:
{'nome': 'Neymar', 'idade': 29, 'time': 'PSG'}
<class 'dict'>
```

```python
# Podemos usar as duas formas juntas
def funcao(*args, **kwargs):
    print(args)
    print(kwargs)

funcao('Brasil', 'Espanha', 'Itália', competicao='Copa do Mundo', ano=2022, pais_sede='Catar')

saída:
('Brasil', 'Espanha', 'Itália')
{'competicao': 'Copa do Mundo', 'ano': 2022, 'pais_sede': 'Catar'}
```

### Desempacotamento
```python
def funcao(param_1, param_2, param_3):
    print(param_1, param_2, param_3)

# Lista
funcao(*['Paula', 'João', 'Hélio'])

saída: Paula João Hélio
```

```python
def funcao(nome, idade):
    print(nome, idade)

# Dicionário
funcao(**{'nome': 'Leandro', 'idade': 30})

saída: Leandro 30
```

### Escopo
```python
# Escopo global
n = 10

def funcao():
    # Escopo local
    n = 55

funcao()

# "n" ainda valerá 10 pois a função tem um "n" diferente do que está fora 
print(n)

saída:  010
```

```python
# Escopo global
n = 10

def funcao():
    # Nesse caso estamos informado que o "n" usado nesse Escopo de Função
    # é o mesmo "n" que está no Escopo Global
    global n
    n = 55

funcao()

# Agora a variável "n" valerá 55
print(n)

saída: 55
```

### Lambda
```python
campeao = lambda times: times[0]
print(campeao(['São Paulo', 'Vasco', 'Corinthians']))

saída: São Paulo
```

```python
soma = lambda n_1, n_2: n_1 + n_2
print(soma(3, 4))

saída: 7
```

### Map, Filter & Reduce
```python
numeros = [1, 2, 3, 4, 5]

# MAP, retorna todos os valores
numeros_mais_um = list(map(lambda n: n + 1, numeros))
print(numeros_mais_um)

saída: [2, 3, 4, 5, 6]
```

```python
numeros = [1, 2, 3, 4, 5]

# FILTER, retorna os valores True
numeros_pares = list(filter(lambda n: n % 2 == 0, numeros))
print(numeros_pares)

saída: [2, 4]
```

```python
# Necessário importar da biblioteca functools
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# REDUCE, retorna um único valor
numeros_somados = reduce(lambda acumulador, atual: acumulador + atual, numeros)
print(numeros_somados)

maior_valor = reduce(lambda anterior, atual: atual if atual > anterior else anterior, numeros)
print(maior_valor)

saída:
15
5
```

## Tratamento de Erro
```python
try:
    valor = 7 / 0
except ZeroDivisionError as e:
    print(f"{e}: Não é possível realizar divisão por ZERO!")
else:
    # Não é necessário fazer no ELSE, pode fazer tudo no TRY
    print(f"O resultado é {valor}")
finally:
    print("Eu sempre serei executado, mesmo se cair no erro.")


saída:
division by zero: Não é possível realizar divisão por ZERO!
Eu sempre serei executado, mesmo se cair no erro.
```

```python
# Podemor encadear vários EXCEPT
try:
    ...
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
```

```python
# Podemos também usar dessa forma o EXCEPT
try:
    ...
except (ZeroDivisionError, TypeError) as e:
    print(e)
```


## Estruturas de Repetição

### For
```python
for fruta in ['banana', 'uva', 'jaca']:
    print(fruta)

saída:
banana
uva
jaca
```

```python
for letra in 'Ana':
    print(letra)

saída:
A
n
a
```

```python
for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"]):
    print(indice, curso)

saída:
0 Python
1 Java
2 HTML
3 PHP
```

```python
# Começar a contar do 1
for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"], start=1):
    print(indice, curso)

saída:
1 Python
2 Java
3 HTML
4 PHP
```

```python
for n in range(3):
    print(n)

saída:
0
1
2
```

```python
for n in range(1, 3):
    print(n)

saída:
1
2
```

```python
for n in range(2, 11, 2):
    print(n)

saída:
2
4
6
8
10
```

```python
for n in range(3, 0, -1):
    print(n)

saída:
3
2
1
```

```python
for letra in ['a', 'c', 'a', 'b', 'd', 'a']:
    if letra == 'a':
        # Faz com que o valor seja pulado, e não exibido
        continue
    print(letra)

saída:
c
b
d
```

```python
for letra in ['a', 'c', 'a', 'b', 'd', 'a']:
    if letra == 'b':
        # Encerra o laço de repetição asism que encontrar o valor
        break
    print(letra)

saída:
a
c
a
```


## Estruturas de Condição

### WHILE
```python
c = 1

while c < 4:
    # Enquanto a variável "c" for menor que 4 ela será exibida
    print(c)
    # NÃO pode esquecer de mudar o valor da variável "c" a cada repetição
    # Caso contrário o loop nunca vai terminar
    c += 1

saída:
1
2
3
```

```python
# Esse loop só será encerrado quando o usuário digitar a letra "s"
while True:
    entrada = input("Deseja sair? [s/n]")
    if entrada.strip().lower() == "s":
        break
```

### IF, ELIF, & ELSE
* Quando queremos realizar uma série de verificações distintas

```python
nota = 2

if nota >= 6:
    print('Aprovado')
elif nota == 5:
    print('Recuperação')
else:
    print('Reprovado')

saída:
Reprovado
```

## Estrutura de Condicão Case
* Quando queremos comparar a mesma variável ou expressão com várias opções

```python
semana = 3

match semana:
    case 1:
        print('Domingo')
    case 2: 
        print('Segunda-feira')
    case 3: 
        print('Terça-feira')
    case 4: 
        print('Quarta-feira')
    case 5: 
        print('Quinta-feira')
    case 6: 
        print('Sexta-feira')
    case 7: 
        print('Sábado')
    case _:
        print('Semana inválida')

saída: Terça-feira
```

### Operador Ternário
```python
numero = 7
print('PAR' if numero % 2 == 0 else 'ÍMPAR')

saída:
ÍMPAR
```


## Orientação a Objeto
* PascalCase

![poo](https://user-images.githubusercontent.com/69995549/147306746-0c08ef82-cac8-4a4f-adc6-d43026fd2474.png)

```python
class Pessoa:
    # Método construtor, é invocado assim que criar uma instância
    def __init__(self, nome):
        # Atributo de Instância, cada objeto terá o seu valor
        self.nome = nome

    def exibir_nome(self):
        print(self.nome)


# Criando uma instância da classe Pessoa, tornando a variável pessoa_1 em um objeto
pessoa_1 = Pessoa('Paula')

# Usando um método público da classe Pessoa
pessoa_1.exibir_nome()

saída: Paula
```

### Encapsulamento
```python
class Pessoa:
    def __init__(self, nome, cpf) -> None:
        # Atributo público
        self.nome = nome
        # atributo privado
        self.__cpf = cpf

    # Método privado, somente acessível na classe
    def __verificar_cpf(self):
        if self.__cpf == '1234':
            return True
        return False

    # Método público, acessível através da instância
    def cpf_existe(self):
        if self.__verificar_cpf():
            print('CPF válido!')
        else:
            print('CPF inválido!')


pessoa_2 = Pessoa('Maria', '1234')
pessoa_2.cpf_existe()

pessoa_3 = Pessoa('Carlos', '7777')
pessoa_3.cpf_existe()

saída:
CPF válido!
CPF inválido!
```

```python
class Calculadora:
    # Somente esse método será acessível
    def calcular(self, op, n1, n2):
        if op == '+':
            return self.__adicionar(n1, n2)
        elif op == '-':
            return self.__subtrair(n1, n2)
        else:
            print('Operação inválida.')

    # Esses métodos não vão ser acessíveis
    def __adicionar(self, n1, n2):
        return n1 + n2

    def __subtrair(self, n1, n2):
        return n1 - n2
```

### Getters & Setters & Estados
* Nome da classe devem ser substantivo
* Nome dos métodos devem ser verbos

```python
class Alarme:
    def __init__(self) -> None:
        self.__estado = False

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        # Método que verifica se um valor pertence a uma classe epecífica
        if isinstance(valor, bool):
            self.__estado = valor


alarme_1 = Alarme()
print(alarme_1.get_estado())
alarme_1.set_estado(True)
print(alarme_1.get_estado())

saída:
False
True
```

### Princípio de Design SOLID
* Código Limpo
* Cada método é responsável por uma única ação

```python
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__inidcar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        ...

    def __inidcar_erro(self):
        ...
```

### Atributo e Método de Classe
```python
class Pessoa:
    # Atributo de classe
    estatico = 'Sousa'

    def __init__(self, nome):
        self.dinamico = nome


pessoa_1 = Pessoa('Maria')
pessoa_2 = Pessoa('Fábio')
# Ambos objetos vão ter o mesmo valor para o atributo de classe
print(pessoa_1.dinamico, pessoa_1.estatico)
print(pessoa_2.dinamico, pessoa_2.estatico)


pessoa_3 = Pessoa('João')
pessoa_4 = Pessoa('Clara')
# Vai ser alterado o valor do atributo de classe de ambos os objetos
# Mesmo eles tendo sido criados antes da alteração
Pessoa.estatico = 'Andrade'
print(pessoa_3.dinamico, pessoa_3.estatico)
print(pessoa_4.dinamico, pessoa_4.estatico)


pessoa_5 = Pessoa('Ronaldo')
pessoa_6 = Pessoa('Adriano')
pessoa_7 = Pessoa('Luiz')
# Todos os demais objetos vão ter esse valor
Pessoa.estatico = 'Imperador'
# Nesse caso, somente o obejto_5 sofrerá alteração no atributo de classe
pessoa_5.estatico = 'Nazário'
print(pessoa_5.dinamico, pessoa_5.estatico)
print(pessoa_6.dinamico, pessoa_6.estatico)
print(pessoa_7.dinamico, pessoa_7.estatico)


saída:
Maria Sousa
Fábio Sousa

João Andrade
Clara Andrade

Ronaldo Nazário
Adriano Imperador
Luiz Imperador
```

```python
class Pessoa:
    estatico = 'Sousa'

    def __init__(self, nome):
        self.dinamico = nome

    # Decorador que permite acessar um atributo de classe dentro da classe
    # o self não funciona com atributos de classe
    @classmethod
    def alterar_estatico(cls, novo_valor):
        cls.estatico = novo_valor


pessoa_5 = Pessoa('Ronaldo')
pessoa_6 = Pessoa('Adriano')
pessoa_7 = Pessoa('Luiz')

Pessoa.estatico = 'Imperador'

# Dessa forma, agora todos os objetos vão ter o memso valor de atributo estático
# Agora o objeto tem controle sobre o contexto de classe
pessoa_5.alterar_estatico('Nazário')

print(pessoa_5.dinamico, pessoa_5.estatico)
print(pessoa_6.dinamico, pessoa_6.estatico)
print(pessoa_7.dinamico, pessoa_7.estatico)

saída:
Ronaldo Nazário
Adriano Nazário
Luiz Nazário
```


### Método Estático
```python
class Saudacao:

    # Não é possível interagir com classe, não dá para usar self ou cls
    @staticmethod
    def exbir_mensagem():
        print('Salve galera!')
```

```python
# Métodos estáticos podem ser usados sem criar uma instância da classe
Saudacao.exbir_mensagem()

saída: Salve galera!
```

### Associação de Classes
```python
from typing import Type


class Interruptor:
    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print(f'Acendendo a luz do {self.__comodo}')

    def apagar(self):
        print(f'Apagando a luz do {self.__comodo}')


class Pessoa:
    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


pessoa = Pessoa()
interruptor_1 = Interruptor('Quarto')

# Aassociação, o objeto pessoa usará os métodos do obeto interruptor
pessoa.acender_luz(interruptor_1)
pessoa.apagar_luz(interruptor_1)

# Método do próprio objeto pessoa
pessoa.dormir()

saída:
Acendendo a luz do Quarto
Apagando a luz do Quarto
Fui dormir...
```

### Princípio Aberto/Fechado - SOLID
```python
class Circo:
    # Fechado, pois já estão definidas as opções
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        elif tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show.')

    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show.')
```

```python
class Circo:
    # Aberto, pois é infinto as opções a serem apresentadas
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando seu show.')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando seu show.')


circo = Circo()
palhaco = Palhaco()
malabarista = Malabarista()

# A fragilidade dessa abordagem de associação é que toda classe passada para o
# objeto circo, obrigatoriamente deve ter o método apresentar_show
circo.apresentar(palhaco)
circo.apresentar(malabarista)

saída:
Palhaço apresentando seu show.
Malabarista apresentando seu show.
```

#### Uso real do Princípio Aberto/Fechado
```poweshell
projeto
      L databases
                L postgre.py
                L sqlserver.py
      main.py
      repositorio.py
```

```python
# databases/postgre.py

class PostgreSQL:
    def __init__(self) -> None:
        self.__conexao = 'PostgreSQL'

    def conectar(self) -> str:
        print('Conectando ao PostgreSQL')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do PostgreSQL')
```

```python
# databases/sqlserver.py

class SQLServer:
    def __init__(self) -> None:
        self.__conexao = 'SQLServer'

    def conectar(self) -> str:
        print('Conectando ao SQLServer')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do SQLServer')
```

```python
# databases/__init__.py

# Vai fazer com que as classes fiquem visíveis fora do pacote databases
from .postgres import PostgreSQL
from .sqlserver import SQLServer
```

```python
# repositorio.py

class Repositorio:
    def select(self, db_connection: any) -> None:
        conn = db_connection.conectar()
        # Realizar ações...
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conn = db_connection.conectar()
        # Realizar ações...
        db_connection.desconectar()
```

```python
# main.py

# Vai fazer com que as classes fiquem visíveis fora do pacote databases
from repositorio import Repositorio
from databases import PostgreSQL
from databases import SQLServer

# A classe Repositorio vai realizar suas ações independente do banco de dados

db_postgre = PostgreSQL()
repo = Repositorio()
repo.insert(db_postgre)
repo.select(db_postgre)

db_sqlserver = SQLServer()
repo = Repositorio()
repo.insert(db_sqlserver)
repo.select(db_sqlserver)
```

### Injeção de Dependência
```python
from typing import Type


class Casa:
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


class Pessoa:
    # Injeção de dependência ocorre quando outra classe faz parte do construtor
    def __init__(self, nome: str, casa: Type[Casa]):
        self.__nome = nome
        self.__casa = casa

    def get_endereco(self):
        print(self.__casa.get_endereco())


casa = Casa('Av. Paulista, 200 - São Paulo/SP')
pessoa = Pessoa('Paula', casa)
pessoa.get_endereco()

saída: Av. Paulista, 200 - São Paulo/SP
```

### Associação Bidirecional
```python
class Casa:
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco
        self.__proprietario = None

    def get_endereco(self):
        print(self.__endereco)
    
    def get_proprietario(self):
        self.__proprietario.get_nome()

    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario


class Pessoa:
    # Injeção de dependência ocorre quando outra classe faz parte do construtor
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__casa = None

    def get_nome(self):
        print(self.__nome)

    def get_endereco(self):
        self.__casa.get_endereco()

    def set_casa(self, casa: any):
        self.__casa = casa


casa_1 = Casa('Av. Jabaquara, 1400 - São Paulo/SP')
pessoa_1 = Pessoa('Henrique')

# A casa receberá um objeto pessoa
casa_1.set_proprietario(pessoa_1)
# A pessoa receberá um obejto casa
pessoa_1.set_casa(casa_1)

# Agora a casa tem acesso a pessoa associada a ela
casa_1.get_proprietario()
# E também a pessoa terá acesso a casa associada a ela
pessoa_1.get_endereco()

saída:
Henrique
Av. Jabaquara, 1400 - São Paulo/SP
```

## Herança
* `self.__` Privado
* `self._` Protegido
* `self.` Público

| | Privado (-) | Protegido (#) | Público (+)
:- | :-: | :-: |  :-: |
Classe | X | X | X
Herança | | X | X
Objeto | | só em Python :(| X

```python
class Avo:
    def __init__(self):
        self.__nome = 'Paulo'
        self._idade = 50
        self.sobrenome = 'Macedo'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


class Pai(Avo):
    def __init__(self):
        super().__init__()
        self.__nome = 'Pedro'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


class Filho(Pai):
    def __init__(self):
        super().__init__()
        self.__nome = 'Thiago'

    def exibir_nome(self):
        print(self.__nome, self.sobrenome)


pai = Pai()
pai.exibir_nome()

# sobrenome vai estar disponível em todos herdeiros
avo = Avo()
avo.exibir_nome()

filho = Filho()
filho.exibir_nome()

saída:
Pedro Macedo
Paulo Macedo
Thiago Macedo
```

### Polimorfismo

### Métodos e Classes Abstratas
* Uma classe abstrata não pode ser instanciada, somente serve para servir de herança
* Um método abstrato é OBRIGATÓRIO ser implementando no herdeiro

```python
from abc import ABC, abstractmethod


class Pai(ABC):
    def __init__(self):
        self.sobrenome = 'Alves'

    def saudacao(self):
        print('Bom dia!')

    # É obrigatório 1 método abstrato para a classe de fato ser abstrata
    @abstractmethod
    def exibir_nome(self) -> None:
        pass


class Filho(Pai):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    # É obrigatório implementar esse método
    def exibir_nome(self) -> None:
        print(self.nome, self.sobrenome)


filho = Filho('Carlos')
filho.exibir_nome()
filho.saudacao()

saída:
Carlos Alves
Bom dia!
```

### Interface
```python
from abc import ABC, abstractmethod
from typing import Type


class FormasInterface(ABC):
    # É caracterizado uma interface quando todos os métodos são abstratos
    @abstractmethod
    def get_perimetro(self) -> int:
        pass

    @abstractmethod
    def get_area(self) -> int:
        pass


class TerrenoQuadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_perimetro(self) -> int:
        return self.lado * 4

    def get_area(self) -> int:
        return self.lado * self.lado


class TerrenoRetangular(FormasInterface):
    def __init__(self, largura: int, comprimento: int) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self) -> int:
        return (self.comprimento * 2) + (self.largura * 2)

    def get_area(self) -> int:
        return self.largura * self.comprimento


class Engenheiro:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu o perimetro: {terreno.get_perimetro()} m.')

    def medir_area(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu a área: {terreno.get_area()} m².')


engenehiro = Engenheiro('Marcos')

terreno_quadrado = TerrenoQuadrado(4)
terreno_retangular = TerrenoRetangular(2, 3)

engenehiro.medir_area(terreno_quadrado)
engenehiro.medir_perimetro(terreno_retangular)

saída:
Marcos mediu a área: 16 m².
Marcos mediu o perimetro: 10 m.
```

### Agregação de Classes
```python
from typing import Type


class Produto:
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor

    def informacoes_produto(self) -> None:
        print(f'Produto: {self.nome} / valor: R$ {self.valor:.2f}')


class Carrinho:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        total = 0

        for produto in self.__produtos:
            produto.informacoes_produto()
            total += produto.valor

        print('Total: R$', total)

        self.__produtos.clear()


tv = Produto('TV LG', 1_350.99)
celular = Produto('Celular iPhone X', 3_600.70)
tinta = Produto('Cartucho impressora HP', 35)

carrinho = Carrinho()
carrinho.adicionar_produto(tv)
carrinho.adicionar_produto(celular)
carrinho.adicionar_produto(tinta)

carrinho.finalizar_compra()

saída:
Produto: TV LG / valor: R$ 1350.99
Produto: Celular iPhone X / valor: R$ 3600.70    
Produto: Cartucho impressora HP / valor: R$ 35.00
Total: R$ 4986.69
```

### Composição de Classes
```python
class Select:
    def select_one(self):
        print('SELECT * FROM database_name')

    def select_many(self):
        print("SELECT * FROM database_name WHERE column_name = 'blá blá blá'")


class Repositorio:
    def __init__(self):
        # instância de uma classe dentro de outra é composição
        # uma forma de fugir da herança
        self.__select = Select()

    def select_all(self):
        return self.__select.select_many()
```

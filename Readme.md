# Python Fundamentos

## Comentários
```python
# Comentário de uma linha

"""
Comentário
de
múltiplas linhas
com aspas duplas
"""

'''
Comentário
de
múltiplas linhas
com aspas simples
'''
```

## Variável
Para declarar uma variável em Python por conveção devemos seguir o padrão **Snake case** caso ela seja composta por mais de uma palavra.
```python
primeiro_nome = "Weverton"
segundo_nome = "Teixeira"
nome_completo = "Weverton Teixeira"
idade = 30
peso = 60.57
```

## Constante
Para declarar uma constante em Python por conveção devemos escrve-lá em letras maisúculas e seguir o padrão **Snake case** caso ela seja composta por mais de uma palavra.
```python
CONEXAO_BANCO_DE_DADOS = "..."
PI = 3.14
```

```python
nome = "Weverton"
del nome
nome  # NameError: name 'nome' is not defined
```


## String
Podemos criar um valor String em Python com aspas duplas ou simples.
```python
nome_completo = "Weverton Teixeira"
COR = 'preta'
```
### Métodos
```python
"arroz".upper()  # ARROZ
"MARACUJÁ".lower()  # maracujá
"weverton".capitalize()  # Weverton
"banana".count("a")  # 3
"banana".count("A")  # 0
"carro".endswith("o")  # True
"carro".endswith("O")  # False
"avião".endswith("a")  # True
"avião".endswith("A")  # False
"11955553333".isalnum()  # True
"1195555-3333".isalnum()  # False
"abacaxi".index("x")  # 5
"abacaxi".index("a")  # 0  # retorna o índice da primeira letra "a" encontrada
"98e".isnumeric()  # False
"98".isnumeric()  # True
"São Paulo - RJ".replace("RJ", "SP")  # São Paulo - SP
"uva maçã pêra".split(" ")  # ['uva', 'maçã', 'pêra']  # O parâmetro passado foi o espaço entre as palavras para criar uma lista
"cebola;alho;cheiro-verde".split(";")  # ['cebola', 'alho', 'cheiro-verde']
```

## Int e Float
Existem dois tipos numéricos em Python, int e float.
```python
inteiro = 7
flutuante = 13.99
```
### Métodos
O método round() é interno do Python e não pertence as classes numérica, ele serve para arredondar um valor flutuante para quantas casas decimais a gente definir, caso não passe o número de casas decimais ele arredonda para o valor inteiro mais próximo.
```python
numero = 9.7483020
round(numero, 2)  # 9.75
round(numero)  # 10
```
Podemos importar bibliotecas para dentro do no nosso script Python para trabalhar com nosso código. A biblioteca math já vem instalada junto ao Python então não precisamos instalar nada.  
Vamos usar dois métodos que pertencem a essa biblioteca:
1. ceil() arredonda para o maior número inteiro mais próximo
2. floor() arredonda para o menor número inteiro mais próximo
```python
import math

numero = 9.9483020
math.ceil(meu_numero)  # 10
math.floor(meu_numero)  # 9
```

## Concatenação
### Usando o sinal `+`
```python
nome = "Weverton"
sobrenome = "Teixeira"
nome_completo = nome + " " + sobrenome  # Weverton Teixeira
```
### Usando o método `.format()`
```python
nome = "Weverton"
sobrenome = "Teixeira"
nome_completo = "{} {}".format(nome, sobrenome)  # Weverton Teixeira

nome_completo = "{} {}"
nome = "Paula"
sobrenome = "Silva"
nome_completo.format(nome, sobrenome)  # Paula Silva
```
### Usando o `fstring`
```python
nome = "Maria"
sobrenome = "Clara"
nome_completo = f"{nome} {sobrenome}"  # Maria Clara

item = "arroz"
preco = 24.99
quantidade = 2
detalahe_compra = f"{item} {preco} {quantidade} R$ {preco * quantidade}"  # arroz 24.99 2 R$ 49.98
```

## Estruturas de Condição
### `if` `elif` e `else`
```python
nota = 6.5

if nota > = 7.0:
    situacao = "Aprovado"
elif nota > 5.0:
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"
    
situacao  # Em recuperação
```
### Operador Ternário: <conteúdo> `if` <condição> `else` <conteúdo>
```python
idade = 15
situacao = "Maior de idade" if idade >= 18 else "Menor de idade"
situacao  # Menor de idade
```

## Coleções
### Listas
```python
lista = ["banana", "uva", "abacaxi"]
type(lista)  # <class 'list'>
lista  # ['banana', 'uva', 'abacaxi']
```
```python
lista = list("aeiou")
type(lista)  # <class 'list'>
lista  # ['a', 'e', 'i', 'o', 'u']
```
```python
lista = []
type(lista)  # <class 'list'>
lista  # []

lista.append("preta")
lista.append("vermelha")
lista  # ['preta', 'vermelha']

lista.insert(0, 'azul')
lista  # ['azul', 'preta', 'vermelha']
```
```python
lista = ["a", "a"]
lista[1] = "A"
lista  # ['a', 'A']
```
```python
lista = ["ovo", "carne", "alface", "manteiga", "arroz", "feijão"]
del lista[1]
lista  # ['ovo', 'alface', 'manteiga', 'arroz', 'feijão']

lista.remove('alface')
lista  # ['ovo', 'manteiga', 'arroz', 'feijão']

valor = lista.pop()
valor  # feijão
lista  # ['ovo', 'manteiga', 'arroz']

valor = lista.pop(0)
valor  # ovo
lista  # ['manteiga', 'arroz']
```
```python
lista = ["dia"]
nova_lista = ["noite", "tarde"]
outra_lista = lista + nova_lista
outra_lista  # ['dia', 'noite', 'tarde']
```
```python
lista = ["chuva"]
nova_lista = ["nublado", "sol"]
lista.extend(nova_lista)
lista  # ['chuva', 'nublado', 'sol']
```
```python
lista = ["uva", "pêra", "uva", "maçã", "uva", "morango"]
uvas = lista.count("uva")
uvas  # 3
```
```python
lista = ["carro", "moto"]
nova_lista = lista.copy()
lista.clear()
lista  # []
nova_lista  # ['carro', 'moto']
```
```python
lista = ["i", "u", "a", "e", "o"]
lista.sort()
lista  # ['a', 'e', 'i', 'o', 'u']
```
```python
lista = ["i", "u", "a", "e", "o"]
lista.sort(reverse=True)
lista  # ['u', 'o', 'i', 'e', 'a']
```
```python
lista = ["Primeiro", "Segundo", "Terceiro"]
lista.reverse()
lista  # ['Terceiro', 'Segundo', 'Primeiro']
```
```python
lista = ["Ana", "Clara", "Bia"]
indice = lista.index("Bia")
indi)  # 2
nome = lista[indice]
nome  # Bia
```
```python
lista = ["Neyar Jr.", "Pelé", "Ronaldo", "Kaká"]
tamanho = len(lista)
tamanho  # 4
```
```python
lista = ['Ana', 1.7, "bolo", True, 8, False]
lista  # ['Ana', 1.7, 'bolo', True, 8, False]
```
```python
lista = [["a","e", "i"], [14, 56, 200]]
lista  # [['a', 'e', 'i'], [14, 56, 200]]
lista[0]  # ['a', 'e', 'i']
lista[0][2]  # i
lista[1]  # [14, 56, 200]
lista[1][1]  # 56
tamanho = len(lista)
tamanho  # 2
```
```python
lista = [1, 2, 3]
nova_lista = lista
nova_lista[0] = 50
lista  # [50, 2, 3]
```

### Dicionários
```python
dicionario = {"nome": "Paula", "idade": 25, "tamanho": 1.57}
type(dicionario)  # <class 'dict'>
dicionario  # {'nome': 'Paula', 'idade': 25, 'tamanho': 1.57}
```
```python
dicionario = dict([("dia", 10), ("mes", 5), ("ano", 2021)])
type(dicionario)  # <class 'dict'>
dicionario  # {'dia': 10, 'mes': 5, 'ano': 2021}
```
```python
dicionario = {}
dicionario["cor"] = "preta"
dicionario["sexo"] = "masculino"
type(dicionario)  # <class 'dict'>
dicionario  # {'cor': 'preta', 'sexo': 'masculino'}
```
```python
dicionario = {"nome": "Pedro Muller"}
novo_dicionario = {"cidade": "Bahia"}
dicionario.update(novo_dicionario)
dicionario  # {'nome': 'Pedro Muller', 'cidade': 'Bahia'}
```
```python
dicionario = {"nome": "Paula", "idade": 25}
dicionario.clear()
dicionario  # {}
```
```python
dicionario = {"nome": "Paula", "idade": 25, "endereco": {"logr": "Rua Tietê", "numero": 174}}

chaves = dicionario.keys()
chaves  # dict_keys(['nome', 'idade', 'endereco'])

valores = dicionario.values()
valores  # dict_values(['Paula', 25, {'logr': 'Rua Tietê', 'numero': 174}])
type(valores)  # <class 'dict_values'>
# valores[0]  # TypeError: 'dict_values' object is not subscriptable

valores = list(valores)
type(valores)  # <class 'list'>
valores[0]  # Paula
```
```python
dicionario = {"nome": "Paula", "idade": 25, "tamanho": 1.57}
for chave, valor in dicionario.items():
    print(chave, valor)
# nome Paula
# idade 25
# tamanho 1.57
```
```python
dicionario = {"nome": "Paula", "idade": 25, "tamanho": 1.57, "sexo": "feminino"}

tamanho = dicionario.pop("tamanho", "Não encontrado")
tamanho  # 1.57
cor = dicionario.pop("cor", "Não encontrado")
cor  # Não encontrado
dicionario  # {'nome': 'Paula', 'idade': 25, 'sexo': 'feminino'}

del dicionario["idade"]
dicionario  # {'nome': 'Paula', 'sexo': 'feminino'}

item_removido = dicionario.popitem()
item_removido  # ('sexo', 'feminino')
dicionario  # {'nome': 'Paula'}
```
```python
dicionario = {"sp": "São Paulo", "rj": "Rio de Janeiro"}
valor = dicionario.get("rj", "Não encontrado.")
valor  # Rio de Janeiro
valor = dicionario.get("ba", "Não encontrado.")
valor  # Não encontrado.
```
```python
dicionario = {"marca": "Fiat", "modelo": "Uno", "cor": "verde", "ano": 1997, "valor": 8763.99}
novo_dicionario = dicionario.copy()
dicionario.clear()
dicionario  # {}
novo_dicionario  # {'marca': 'Fiat', 'modelo': 'Uno', 'cor': 'verde', 'ano': 1997, 'valor': 8763.99}
```
```python
dicionario = {"item_1": "arroz", "item_2": "feijão", "item_3": "café"}
tamanho = len(dicionario)
tamanho  # 3
```
```python
dicionario = {"e": 2, "u": 5, "a": 1, "o": 4, "i": 3}

sorted(dicionario.keys())  # ['a', 'e', 'i', 'o', 'u']
sorted(dicionario.keys(), reverse=True)  # ['u', 'o', 'i', 'e', 'a']

sorted(dicionario.values())  # [1, 2, 3, 4, 5]
sorted(dicionario.values(), reverse=True)  # [5, 4, 3, 2, 1]

sorted(dicionario.items())  # [('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
dict(sorted(dicionario.items()))  # {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

sorted(dicionario.items(), reverse=True)  # [('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]
dict(sorted(dicionario.items(), reverse=True))  # {'u': 5, 'o': 4, 'i': 3, 'e': 2, 'a': 1}

sorted(dicionario.items(), key=lambda item: item[1])  # [('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)]
dict(sorted(dicionario.items(), key=lambda item: item[1]))  # {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

sorted(dicionario.items(), reverse=True, key=lambda item: item[1])  # [('u', 5), ('o', 4), ('i', 3), ('e', 2), ('a', 1)]
dict(sorted(dicionario.items(), reverse=True, key=lambda item: item[1]))  # {'u': 5, 'o': 4, 'i': 3, 'e': 2, 'a': 1}
```
```python
dicionario = {"sp": "São Paulo", "rj": "Rio de Janeiro", "ba": "Bahia"}

chave_existe = True if "rj" in dicionario else False
chave_existe  # True

chave_existe = True if "pe" in dicionario else False
chave_existe  # False

valor_existe = True if "Bahia" in dicionario.values() else False
valor_existe  # True

valor_existe = True if "Maceió" in dicionario.values() else False
valor_existe  # False
```

### Conjuntos
```python
conjunto = {"a", "b", "c", "a"}
type(conjunto)  # <class 'set'>
conjunto  # {'a', 'c', 'b'}
```
```python
conjunto = set([1, 2, 3, 2, 2, 2, 3, 1, 4, 4, 5])
type(conjunto)  # <class 'set'>
conjunto  # {1, 2, 3, 4, 5}
```
```python
conjunto = set()
conjunto.add("uva")
conjunto.add("maracuja")
conjunto.add("uva")
type(conjunto)  # <class 'set'>
conjunto  # {'maracuja', 'uva'}
```
```python
conjunto = {"preta", "verde", "azul", "branca", "amarela"}

conjunto.remove("azul")
conjunto  # {'amarela', 'branca', 'preta', 'verde'}
# conjunto.remove("rosa")  # KeyError: 'rosa'

conjunto.discard("preta")
conjunto  # {'verde', 'branca', 'amarela'}
conjunto.discard("rosa")  # Nãoo gera erro mesmo que não exista
```
```python
conjunto = set([1, 2, 3, 4, 5, 5, 5])
novo_conjunto = conjunto.copy()
conjunto.clear()
conjunto  # set() -> representação de um conjunto vazio
novo_conjunto  # {1, 2, 3, 4, 5}
```
```python
conjunto = set(["Ana", "Ana", "Maria", "Pedro"])
tamanho = len(conjunto)
tamanho  # 3
```
```python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}

C = A.union(B)  # # A ∪ B é o mesmo que: A união com B
C  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

C = A | B  # # A ∪ B é o mesmo que: A união com B
C  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```
```python
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8, 9}

C = A.intersection(B)  # A & B é o mesmo que: A interseção com B (elementos que aparecem em ambos)
C  # {0, 9}

C = A & C
C  # {0, 9}
```
```python
"""
Símbolo matemático | Operador Python | Descrição
----------------------------------------------------------------------
E ∈ S              | in              | elemento E é membro de S
A ⊆ B              | <=              | A é um subconjunto de B
A ⊂ B              | <               | A é um subconjunto próprio de B
A ∪ B              | |               | A união com B
A ∩ B              | &               | A interseção com B
A ∖ B              | -               | diferença entre A e B
"""
```

## Estruturas de Repetição
### `for` <item> `in` <iterável> 
```python
for fruta in ["banana", "uva", "jaca"]:
    print(fruta)
# banana
# uva
# jaca
```
```python
for letra in "Ana":
    print(letra)
# A
# n
# a
```
```python
for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"]):
    print(indice, curso)
# 0 Python
# 1 Java
# 2 HTML
# 3 PHP

for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"], start=1):
    print(indice, curso)
# 1 Python
# 2 Java
# 3 HTML
# 4 PHP
```

```python
for n in range(3):
    print(n)
# 0
# 1
# 2

for n in range(1, 3):
    print(n)
# 1
# 2

for par in range(2, 11, 2):
    print(n)
# 2
# 4
# 6
# 8
# 10

for n in range(3, 0, -1):
    print(n)
# 3
# 2
# 1
```
```python
for letra in ["a", "c", "a", "b", "d", "a"]:
    if letra == "a":
         continue
    print(letra)
# c
# b
# d
```
```python
for letra in ["a", "c", "a", "b", "d", "a"]:
    if letra == "b":
         break
    print(letra)
# a
# c
# a
```

### `while` <condição>
```python
c = 1

while c < 4:
    print(c)
    c += 1
# 1
# 2
# 3
```
```python
while True:
    entrada = input("Deseja sair? [s/n]")
    if entrada.strip().lower() == "s":
        break
```

## Funções
```python
def saudacao():
    print("Olá!")

saudacao()
```
```python
def saudacao(parametro):
    print(f"Olá, {parametro}!")

arguemnto = "Weverton"
saudacao(argumento)
```

### Lambda
```python
soma = lambda n_1, n_2: n_1 + n_2
resultado = lambda(3, 4)
resultado  # 7
```

### Packing (Empacotar) e Unpacking (Desempacotar)
```python
def minha_funcao(*args):
    type(args)  # <class 'tuple'>
    args  # ('bola', 'sacola', 'boné', 'luvas')
    
    # Desempacotando
    item_1, item_2, item_3, item_4 = args
    item_1  # bola
    item_2  # sacola
    item_3  # boné
    item_4  # luvas

minha_funcao("bola", "sacola", "boné", "luvas")
```
```python
def minha_funcao(**kwargs):
    type(kwargs)  # <class 'dict'>
    kwargs  # {'nome': 'Weverton', 'idade': 30, 'peso': 60.49}

minha_funcao(nome="Weverton", idade=30, peso=60.49)
```

## Escopo
```python
# Escopo global
n = 10

def minha_funcao():
    # Escopo local
    n = 55

n  # 10
``` 

## Orientação a Objeto
```
class Car:
    # atributos de classe
    rodas = 4
    portas = 2
    
    # Método construtor
    def __init__(self)
    # atributos de instância
    motor = True


# Instância de uma classe
carro_um = Car()
carro_dois = Car()

# Altera para todas as classe
Car.portas = 4

# Altera somente na instância
carro_um.portas = 2

# Acessando atributos de uma classe, o mesmo serve para os comportamentos (métodos)
carro_um.portas  # 2
carro_dois.portas  # 4

# cada instância tem seu id, por isso que se a gente alterar o atributo de uma instância não aletar de todas
id(carro_um)  # 139971849561744
id(carro_dois)  # 139971849561824

# Verificar se um objeto é a instância de uma certa classe
isinstance(carro_um, Car)  # True
```



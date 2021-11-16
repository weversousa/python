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
primeiro_nome
segundo_nome
nome_completo
idade
preco
```

## Constante
Para declarar uma constante em Python por conveção devemos escrve-lá em letras maisúculas e seguir o padrão **Snake case** caso ela seja composta por mais de uma palavra.
```python
CONEXAO_BANCO_DE_DADOS
PI
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
"abacaxi".index("a")  # 0  # retorno o índice da primeira letra "a" encontrada
"98e".isnumeric()  # False
"98".isnumeric()  # True
"São Paulo - RJ".replace("RJ", "SP")  # São Paulo - SP
"uva maçã pêra".split(" ")  # ['uva', 'maçã', 'pêra']  # O parâmetro passado foi o espaço entre as palavras para criar uma lista
"cebola;alho;cheiro-verde".split(";")  # ['cebola', 'alho', 'cheiro-verde']
```

from operator import itemgetter


''' Forma literal de criar um dicionário '''

produtos = {
    'arroz': 28.90,
    'cafe': 9.90,
}

print(produtos)

# Resultado:
# {'arroz': 28.9, 'cafe': 9.9}
# -----------------------------------------------------------------------------

''' Criando um dicionário através do método dict '''

produtos_novos = dict([('tomate', 2.89), ('shampoo', 12.99)])
print(produtos_novos)

# Resultado:
# {'tomate': 2.89, 'shampoo': 12.99}
# -----------------------------------------------------------------------------

''' Forma tradicional de criar um dicionário '''

mais_produtos = {}
mais_produtos['leite'] = 3.40
print(mais_produtos)

# Resultado:
# {'leite': 3.4}
# -----------------------------------------------------------------------------

''' Juntando dicionários '''

produtos.update(produtos_novos)
print(produtos)

# Resultado:
# {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99}
# -----------------------------------------------------------------------------

''' Juntando dicionários '''

for produto, valor in mais_produtos.items():
    produtos[produto] = valor

print(produtos)

# Resultado:
# {'arroz': 28.9, 'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
# -----------------------------------------------------------------------------

''' Acessando chaves de um dicionário '''

print(produtos.get('cafe', 'Chave não encontrada.'))
print(produtos.get('nescau', 'Chave não encontrada.'))

# Resultado:
# 9.9
# Chave não encontrada.
# -----------------------------------------------------------------------------

''' Verificando se uma chave existe '''

print('leite' in produtos)

# Resultado:
# True
# -----------------------------------------------------------------------------

''' Verificando se um valor existe '''

print(3.40 in produtos.values())

# Resultado:
# True
# -----------------------------------------------------------------------------

''' Deletando - no caso do del se não existir gera um erro '''

del produtos['arroz']
print(produtos)

# Resultado:
# {'cafe': 9.9, 'tomate': 2.89, 'shampoo': 12.99, 'leite': 3.4}
# -----------------------------------------------------------------------------

''' Deletando - Com pop não gera erro caso não exista e retona o valor '''

print(produtos.pop('tomate', 'Produto não encontrado'))
print(produtos.pop('melancia', 'Produto não encontrado'))
print(produtos)

# Resultado:
# 2.89
# Produto não encontrado
# {'cafe': 9.9, 'shampoo': 12.99, 'leite': 3.4}
# -----------------------------------------------------------------------------

''' Compreensão de Dicionário '''

frutas = [('maça', 2.90), ('uva', 7.90), ('mamao', 5.90), ('pera', 4.43)]

valor_total = {fruta[0].capitalize(): fruta[1] * 2 for fruta in frutas}

print(valor_total)

# Resultado:
# {'Maça': 5.8, 'Uva': 15.8, 'Mamao': 11.8, 'Pera': 8.86}
# -----------------------------------------------------------------------------

''' Ordernar um dicionário pela Chave '''

frutas_ordenadas = dict(
    sorted(valor_total.items(), key=itemgetter(0))
)

print(frutas_ordenadas)

# Resultado:
# {'Maça': 5.8, 'Uva': 15.8, 'Mamao': 11.8, 'Pera': 8.86}
# -----------------------------------------------------------------------------

''' Ordernar um dicionário pelo Valor '''

frutas_ordenadas = dict(
    sorted(valor_total.items(), key=itemgetter(1))
)

print(frutas_ordenadas)

# Resultado:
# {'Maça': 5.8, 'Pera': 8.86, 'Mamao': 11.8, 'Uva': 15.8}
# -----------------------------------------------------------------------------

''' Ordernar um dicionário pelo Valor de forma DECRESCENTE '''

frutas_ordenadas = dict(
    sorted(valor_total.items(), key=itemgetter(1), reverse=True)
)

print(frutas_ordenadas)

# Resultado:
# {'Uva': 15.8, 'Mamao': 11.8, 'Pera': 8.86, 'Maça': 5.8}

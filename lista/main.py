''' Forma Lietal de criar uma lista '''

frutas = ['maçã', 'uva', 'abacaxi']
print(frutas)

# Resultado:
# ['maçã', 'uva', 'abacaxi', 'abacate']
# -----------------------------------------------------------------------------

''' Em Python as listas são heterogêneas (não é boa prática) '''

heterogenea = ['Paula', 3, 5.8, {'legume': 'cenoura'}, frutas]
print(heterogenea)

# Resultado:
# ['Paula', 3, 5.8, {'legume': 'cenoura'}, ['maçã', 'uva', 'abacaxi']]
# -----------------------------------------------------------------------------

''' O método list cria uma lista - Para isso deve ser um parâmetro iterável '''

numeros = list('123456789')
print(numeros)

# Resultado
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# -----------------------------------------------------------------------------

''' Acessando valores pelo índice '''

print(frutas[0], frutas[1])

# Resultado
# maçã uva
# -----------------------------------------------------------------------------

''' Percorrendo com um laço '''

for fruta in frutas:
    print(fruta, end=' ')

# Resultado
# maçã uva abacaxi
# -----------------------------------------------------------------------------

''' Verificar se um valor está na lista '''

if 'uva' in frutas:
    print('SIM')

# Resultado:
# SIM
# -----------------------------------------------------------------------------

''' Alterando valores a lista '''

frutas[2] = 'banana'
print(frutas)

# Resultado:
# ['maçã', 'uva', 'banana']
# -----------------------------------------------------------------------------

''' Add valores a lista '''

frutas.append('pêra')
print(frutas)

# Resultado:
# ['maçã', 'uva', 'banana', 'pêra']
# -----------------------------------------------------------------------------

''' A lista do Python é uma Classe e asism possue Métodos '''

clubes = []

''' Inserindo valores pelo índice '''

clubes.insert(0, 'São Paulo')
clubes.insert(1, 'Vasco')

print(clubes)

''' Tamanho da lista '''

print(len(clubes))

# Resultado:
# ['São Paulo', 'Vasco']
# 2
# -----------------------------------------------------------------------------

''' Removendo pelo índice, O método pop retorna o valor '''
''' Se não existir gera um erro '''

clubes.pop(1)
del clubes[0]
# -----------------------------------------------------------------------------

''' Compreensão de Lista '''

pares = [numero * 3 for numero in range(1, 11, 1) if numero % 2 == 0]

print(pares)

# Resultado:
# [6, 12, 18, 24, 30]


listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

impares = [numero for lista in listas for numero in lista if numero % 2 != 0]

print(impares)

# Resultado:
# [1, 3, 5, 7, 9]

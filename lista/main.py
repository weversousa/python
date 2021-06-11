frutas = ['maçã', 'uva', 'abacaxi', 'abacate']

frutas[0]  # maçã
frutas[3]  # abacate
# frutas[4] # IndexError: list index out of range


# Em Python as listas são heterogêneas (não é boa prática)
heterog = ['Paula', 3, 5.8, {'legume': 'cenoura'}, frutas]  # ['Paula', 3, 5.8, {'legume': 'cenoura'}, ['maçã', 'uva', 'abacaxi', 'abacate']]


''' A lista do Python é uma Classe e asism possue Métodos '''
times = []

# Adicionando valores pelo índice
times.insert(0, 'São Paulo')
times.insert(1, 'Vasco')

# Tanaho da lista
len(times)  # 2

# Removendo pelo índice
times.pop(1)  # O método pop retorna o valor
del times[0]

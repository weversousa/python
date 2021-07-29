from functools import reduce

numeros = [1, 2, 3, 4, 5]

numeros_mais_um = list(map(lambda n: n + 1, numeros))

print(numeros_mais_um)


numeros_pares = list(filter(lambda n: n % 2 == 0, numeros))
print(numeros_pares)

numeros_somados = reduce(lambda acumulador, valor_atual: acumulador + valor_atual, numeros)
print(numeros_somados)

maior_valor = reduce(lambda anterior, valor_atual: valor_atual if valor_atual > anterior else anterior, numeros)
print(maior_valor)

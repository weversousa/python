# A compreensão de listas é uma maneira elegante de definir e criar listas com
# base em listas existentes.

pares = [numero * 3 for numero in range(1, 11, 1) if numero % 2 == 0]
print(pares)

# Resultado:
# [6, 12, 18, 24, 30]
# -----------------------------------------------------------------------------

listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

impares = [numero for lista in listas for numero in lista if numero % 2 != 0]

print(impares)

# Resultado:
# [1, 3, 5, 7, 9]

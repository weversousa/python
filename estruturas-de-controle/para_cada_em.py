# Para cada número em Lista: Imprima o número.
for numero in [10, 15, 20, 25, 30]:
    print(numero)

# Resultado:
# 10
# 15
# 20
# 25
# 30
# -----------------------------------------------------------------------------

# Para cada número em 1 a 6: Imprima o número. Ele vai até um antes do 6.
for numero in range(1, 6, 1):
    print(numero)

# Resultado:
# 1
# 2
# 3
# 4
# 5
# -----------------------------------------------------------------------------

# Tabuada do 2 - Laço Encadeado
for i in range(2, 3, 1):
    for j in range(1, 11, 1):
        print(f'{i} x {j} = {i * j}')

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

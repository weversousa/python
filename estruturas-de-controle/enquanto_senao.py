contador = 1

while contador < 6:
    if contador == 8:
        break
    print(contador)

    # Se esquecer de acrescer 1 ao contador entra em loop infinito e trava o pc
    contador += 1
else:
    print('Encerrando o laço...')

# Resultado:
# 1
# 2
# 3
# 4
# 5
# Encerrando o laço...
# -----------------------------------------------------------------------------

contador = 1

while contador < 6:
    if contador == 3:
        break
    print(contador)

    # Se esquecer de acrescer 1 ao contador entra em loop infinito e trava o pc
    contador += 1
else:
    print('Só serei executado se não encontrar o número 3')

# Resultado:
# 1
# 2

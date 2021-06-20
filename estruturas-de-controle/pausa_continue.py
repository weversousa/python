# O break para a estrutura quando encontra a condição desejada e sai dela.
for numero in range(1, 7):
    if numero == 4:
        break
    else:
        print(numero)

# Resultado:
# 1
# 2
# 3
# -----------------------------------------------------------------------------

# O continue ele pula o valor da condição e continua a estrutura
for numero in range(1, 7):
    if numero == 4:
        continue
    else:
        print(numero)

# Resultado:
# 1
# 2
# 3
# 5
# 6

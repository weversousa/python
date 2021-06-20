# Uma função recursiva, chama a si até o parâmetro atingir a condição desejada.

def exibir_ola(numero):
    if numero > 5:
        print('Olá')
    else:
        print(f'O numero está valendo {numero}')
        return exibir_ola(numero + 1)


exibir_ola(1)

# Resultado:
# O numero está valendo 1
# O numero está valendo 2
# O numero está valendo 3
# O numero está valendo 4
# O numero está valendo 5
# Olá

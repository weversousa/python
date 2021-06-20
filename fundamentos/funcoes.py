def sem_retorno(nome):
    print(f'Olá {nome}.')


sem_retorno('Weverton')

# Resultado:
# Olá Weverton.
# -----------------------------------------------------------------------------


def com_retorno(n1, n2):
    return n1 + n2


soma = com_retorno(3, 7)
print(soma)

# Resultado:
# 10
# -----------------------------------------------------------------------------


def com_valor_padrao_no_parametro(n1, n2=3):
    return n1 * n2


multiplicacao = com_valor_padrao_no_parametro(4, 5)
print(multiplicacao)

multiplicacao = com_valor_padrao_no_parametro(4)
print(multiplicacao)

# Resultado:
# 20
# 12
# -----------------------------------------------------------------------------

# Função Lambda... Pode ser armazenada em uma variável
campeao = lambda times: times[0]
campeao(['São Paulo', 'Vasco', 'Corinthians'])

# Resultado:
# São Paulo

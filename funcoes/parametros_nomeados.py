# Você pode definer um valor padrão para todos os parâmetros ou só alguns.
def valor_nomeado(n1, n2):
    return n1 + n2


soma = valor_nomeado(n1=1, n2=5)
soma2 = valor_nomeado(n2=4, n1=33)


print(soma, soma2)

# Resultado:
# 6 37

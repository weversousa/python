# Você pode definer um valor padrão para todos os parâmetros ou só alguns.
def valor_padrao(n1=0, n2=0):
    return n1 + n2


soma = valor_padrao(1, 5)
soma2 = valor_padrao()
soma3 = valor_padrao(4)

print(soma, soma2, soma3)

# Resultado:
# 6 0 4

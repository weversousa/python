string = "Texto"  # str

string_2 = 'Texto'  # str

# A String é tratada como Objeto, então ela possui a Notação de Ponto.
nome = 'Weverton'

nome.lower()

# Resultado:
# weverton
# -----------------------------------------------------------------------------

nome.upper()

# Resultado:
# WEVERTON
# -----------------------------------------------------------------------------

nome.center(20, '|')

# Resultado:
# ||||||Weverton||||||
# -----------------------------------------------------------------------------

# Contar quantas vezes um caractere específico aparece em uma String
nome.count('e')

# Resultado:
# 2
# -----------------------------------------------------------------------------

# Múltiplicando String
nome * 5

# Resultado:
# WevertonWevertonWevertonWevertonWeverton
# -----------------------------------------------------------------------------

# Fatiando Strings.
# [início:fim:passo] -> os valos são índices
#  Osasco-SP
# +012345678
# -987654321

cidade_estado = 'Osasco-SP'

cidade = cidade_estado[0:6]

cidade2 = cidade_estado[:6]  # Pode omitir o índice inicial nesse caso

cidade3 = cidade_estado[-9:-3]

print(cidade, cidade2, cidade3)

# Resultado:
# Osasco Osasco Osasco
# -----------------------------------------------------------------------------

estado = cidade_estado[7:9]

estado2 = cidade_estado[7:]  # Pode omitir o índice final nesse caso

print(estado, estado2)

# Resultado:
# SP SP
# -----------------------------------------------------------------------------

# Invertendo uma String
palavra = 'Python'

palavra = palavra[::-1]

print(palavra)

# Resultado:
# nohtyP
# -----------------------------------------------------------------------------

# Pulando índices
numeros = [1, 2, 3, 4, 5, 6]

# Começa do índice 1. Até o último índice. Passando de 2 em 2
impares = numeros[1::2]

print(impares)

# Resultado:
# [2, 4, 6]

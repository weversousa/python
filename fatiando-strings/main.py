'''
[início:fim:passo]

Essas três partes correspondem aos índices de cada caractere em uma String
inclusive os espaços.

Índice Positivo   [01234567]
texto           = "Bom dia!"
Índice Negativo  -[87654321]
'''
#        012345678
texto = 'Osasco-SP'
#       -987654321

print(texto[0])
print(texto[-1])

# Resultado:
# O
# P
# -----------------------------------------------------------------------------

''' Atenção, o índice 6 não entra na contagem '''

print(texto[0:6])
print(texto[-9:-3])

# Resultado:
# Osasco
# Osasco
# -----------------------------------------------------------------------------

''' Quando é omitido o valor, significa que é zero '''

numeros = '123456789'
impares = numeros[::2]
print(impares)

# Resultado:
# 13579

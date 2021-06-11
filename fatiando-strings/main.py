'''
[início:fim:passo]

Esses três partes correspondem aos índices de cada caractere em uma String
inclusive os espaços.

Índice Positivo   [01234567]
texto           = "Bom dia!"
Índice Negativo  -[87654321]
'''
#        012345678
texto = 'Osasco-SP'
#       -987654321


print(texto[0])  # O
print(texto[-1])  # P

# Atenção, o índice 6não entra na contagem, vai até o 5 nesse caso
print(texto[0:6])  # Osasco
print(texto[-9:-3])  # Osasco

# Quando é omitido o valor, significa que é zero
numeros = '123456789'
impares = numeros[::2]
print(impares)

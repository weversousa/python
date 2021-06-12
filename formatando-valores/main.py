'''
:s - String
:d - int
:f - float

> - Esquerda
< - Direita
^ - Centro
'''

''' Duas casas decimais '''

print(f'{ 10 / 3:.2f}')

# Resultado:
# 3.33
# -----------------------------------------------------------------------------

''' Determinar um tamanho fixo de números '''

# Nesse caso eu quero que o meu número tenha 10 caracteres.
# Caso ele não tenha será completado por zeros o que faltar.

print(f'{1:0>10}')

# Resultado:
# 0000000001


print(f'{3:0<10}')

# Resultado:
# 3000000000


print(f'{77:0^10}')

# Resultado:
# 0000770000


print(f'{4:0>10.3f}')

# Resultado:
# 000004.000
# -----------------------------------------------------------------------------

''' Formatando Strings '''

# Vou alinhar os preços e para isso vou deixar a String com 10 caracteres
# Se a fruta não tiver 10 letras, vão ser usados espaços até chegar a 10

fruta_1, fruta_2, fruta_3 = 'Banaba', 'Maça', 'Uva'

print(f'{fruta_1: <10} R$ 2,50')
print(f'{fruta_2: <10} R$ 5,50')
print(f'{fruta_3: <10} R$ 7,50')

# Resultado:
# Banaba     R$ 2,50
# Maça       R$ 5,50
# Uva        R$ 7,50

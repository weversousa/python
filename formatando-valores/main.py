'''
:s - String
:d - int
:f - float

> - Esquerda
< - Direita
^ - Centro
'''

# Exemplo 1: Duas casas decimais
print(f'{ 10 / 3:.2f}')  # 3.33

# Exemplo 2: Determinar um tamanho fixo de números
# Nesse caso eu quero que o meu número tenha o tamanho 10
# E caso ele não tenha o tamho 10 que seja completado por zeros o que faltar
print(f'{1:0>10}')  # 0000000001
print(f'{3:0<10}')  # 3000000000
print(f'{77:0^10}')  # 0000770000
print(f'{4:0>10.3f}')  # 000004.000


# Exemplo 3: Formatando Strings
# Vou alinhar os preços e para isso vou deixar a String com tamanho 10
# Se a frota não tiver 10 letras, vão ser usados espaços até chegar a 10
fruta_1, fruta_2, fruta_3 = 'Banaba', 'Maça', 'Uva'
print(f'{fruta_1: <10} R$ 2,50')
print(f'{fruta_2: <10} R$ 5,50')
print(f'{fruta_3: <10} R$ 7,50')

'''
Resultado do print acima

Banaba     R$ 2,50
Maça       R$ 5,50
Uva        R$ 7,50
'''

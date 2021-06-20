booleano_true = True

booelano_false = False

'''
Além dos valores literais True e False, outros valores em Python podem ser
usados como booleanos.
Para sabermos qual o valor booleano de um determinado tipode dado a gente deve
usar a negação lógica "not".
Quando negamos um valor ele passa a ser booleano.
Então se esse valor é True a sua negação será False.
Para sabermos se um valor é True ou False usamos a "dupla Negação", pois
assim ele volta ao valor lógico original.
Por exemplo: not False vai resultar em True mas not not False resultará False.
'''

# Sempre True
print(not not True)
print(not not 1)  # Qualquer número diferente de Zero, positivo ou negativo
print(not not 'a')
print(not not ' ')
print(not not " ")
print(not not "a")
print(not not ['banada'])
print(not not {'fruta': 'melão'})
print(not not ('azul',))
print(not not [''])
print(not not ('',))
print(not not {'': ''})

print('-' * 20)

# Sempre False
print(not not False)
print(not not 0)
print(not not '')
print(not not "")
print(not not ())
print(not not [])
print(not not {})

print('-' * 20)

# Exemplos de uso
false = not not ('' or 0 or None or [] or {})

verdade = not not ('Paula' or 0 or None or [] or {})

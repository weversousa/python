# A compreensão de dicionário é uma forma elegante e concisa de criar
# dicionários.


frutas = [('maça', 2.90), ('uva', 7.90), ('mamao', 5.90), ('pera', 4.43)]

valor_total = {fruta[0].capitalize(): fruta[1] * 2 for fruta in frutas if fruta[0] != 'uva'}

print(valor_total)

# Resultado:
# {'Maça': 5.8, 'Mamao': 11.8, 'Pera': 8.86}

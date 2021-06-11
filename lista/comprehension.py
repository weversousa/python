''' List Comprehension '''

vogais = 'aeiou'
vogais_separadas = [vogal for vogal in vogais]
print(vogais_separadas) # ['a', 'e', 'i', 'o', 'u']

vogais_separadas_menos_o = [vogal for vogal in vogais if vogal != 'o']
print(vogais_separadas_menos_o)  # ['a', 'e', 'i', 'u']

tabuada = [(chave, valor, chave * valor) for chave in [2] for valor in [1, 2, 3, 4]]
print(tabuada)  # [(2, 1, 2), (2, 2, 4), (2, 3, 6), (2, 4, 8)]

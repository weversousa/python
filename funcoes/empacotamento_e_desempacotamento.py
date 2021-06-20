def varios_dados(*args):
    return args


tupla = varios_dados('a', 3, [3, 5], {'nome': 'Pedro'})
print(tupla)

# Resultado:
# ('a', 3, [3, 5], {'nome': 'Pedro'})
# -----------------------------------------------------------------------------


def varios_dados_chave_valor(**kwargs):
    return kwargs


dicionario = varios_dados_chave_valor(nome='Neymar', idade=29, time='PSG')
print(dicionario)

# Resultado:
# {'nome': 'Neymar', 'idade': 29, 'time': 'PSG'}
# -----------------------------------------------------------------------------


def pegando_tudo(*args, **kwargs):
    print(args)
    print(kwargs)


pegando_tudo('Brasil', 'Espanha', 'Itália', competicao='Copa do Mundo',
             ano=2022, pais_sede='Catar')

# Resultado:
# ('Brasil', 'Espanha', 'Itália')
# {'competicao': 'Copa do Mundo', 'ano': 2022, 'pais_sede': 'Catar'}

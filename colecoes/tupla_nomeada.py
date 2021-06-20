from collections import namedtuple

Estados = namedtuple(typename='Estados', field_names=['sigla', 'nome'])

estado_sp = Estados(sigla='SP', nome='São Paulo')

print(estado_sp)
print(estado_sp.sigla)
print(estado_sp.nome)

# Resultado:
# Estados(sigla='SP', nome='São Paulo')
# SP
# São Paulo
# -----------------------------------------------------------------------------

estado_ba = Estados('BA', 'Bahia')

print(estado_ba)
print(estado_ba.sigla)
print(estado_ba.nome)

# Resultado:
# Estados(sigla='BA', nome='Bahia')
# BA
# Bahia

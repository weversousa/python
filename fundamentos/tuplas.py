'''
Sobre as Tuplas
    Imutável, após criada não pode (adicionar, alterar ou remover)
    Heterogêna
    Acessada por ídices
'''


nao_e_uma_tupla = (1)
print(nao_e_uma_tupla, type(nao_e_uma_tupla))

# Resultado:
# # 1 <class 'int'>
# -----------------------------------------------------------------------------

tupla = (1,)
print(tupla, type(tupla))  # (1,) <class 'tuple'>

# Resultado:
# 
# -----------------------------------------------------------------------------

# Declaração implícita
tupla = 10, 20, 30
print(tupla, type(tupla))

# Resultado:
# (10, 20, 30) <class 'tuple'>
# -----------------------------------------------------------------------------

# Declaração explícita (Boa prática).
tupla = (10, 20, 30)

# Resultado:
# (10, 20, 30)
# -----------------------------------------------------------------------------

# A linha 4 poderia ser assim então.
tupla = 1,

# Resultado:
# (1,)
# -----------------------------------------------------------------------------

# Usando a função tuple. Necessário ser Iterável.
tupla = tuple('aeiou')

# Resultado:
# ('a', 'e', 'i', 'o', 'u')
# -----------------------------------------------------------------------------

tupla = ('BA', 'SP', 'RJ', 'BA', 'MG', 'BA')
contar_elementos = tupla.count('BA')

# Resultado:
# 3
# -----------------------------------------------------------------------------

print('SP' in tupla)

# Resultado:
# True
# -----------------------------------------------------------------------------

# Se tiver mais de um, ele retorna o primeiro.
indice_do_elemento = tupla.index('RJ')

# Resultado:
# 2
# -----------------------------------------------------------------------------

pegar_pelo_indice = tupla[4]

# Resultado:
# MG
# -----------------------------------------------------------------------------


# É possível nomear os elementos de uma Tupla.
# Os exemplos estão na pasta "colecoes" desse Repostório.

# Um set em Python é uma coleção de itens únicos (distintos).


# Criar um Set a partir de uma Lista.
numeros = [1, 2, 1, 3, 4, 2, 1, 3, 2, 5]

numeros_distintos = set(numeros)

print(numeros_distintos)

# Resultado:
# {1, 2, 3, 4, 5}
# -----------------------------------------------------------------------------

# Criar um Conjunto vazio e ir add os valores.
frutas = ['banana', 'maça', 'banana', 'uva', 'banana', 'maça', 'uva', 'pêra']

frutas_distintas = set()

for fruta in frutas:
    frutas_distintas.add(fruta)

print(frutas_distintas)

# Resultado:
# {'maça', 'uva', 'banana', 'pêra'}
# -----------------------------------------------------------------------------

# Forma literal... Note que não é um dicionário, pois não é Chave: Valor

meu_set = {'a', 'e', 'e', 'a', 'i', 'o', 'a', 'i', 'u', 'u'}
print(meu_set)

# Resultado:
# {'u', 'a', 'e', 'i', 'o'}
# -----------------------------------------------------------------------------

# Para remover podemos usar remove(), mas só se tiver certeza, pois gera erro
# caso não encontre o elemento.

numeros = set(['1', '2', '3'])
print(numeros)

numeros.remove('2')
print(numeros)

# Resultado:
# {'1', '3', '2'}
# {'1', '3'}
# -----------------------------------------------------------------------------

# A função dircard(), remove um elemnto mas não gera erro caso não o encontre.

letras = set(['a', 'b', 'c'])
print(letras)

letras.discard('c')
print(letras)

# Resultado:
# {'a', 'c', 'b'}
# {'a', 'b'}
# -----------------------------------------------------------------------------

# Limpar por completo um Set

cores = set(['azul', 'verde', 'preto', 'verde'])
print(cores)

cores.clear()
print(cores)

# Resultado:
# {'preto', 'azul', 'verde'}
# set() <- Representação de um set vazio
# -----------------------------------------------------------------------------

# Operações matemáticas

A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}

# C = A ∪ B é o mesmo que A união com B
C = A.union(B)
print(C)

C = A | B
print(C)

# Resultado:
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# -----------------------------------------------------------------------------

A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8, 9}

# C = A & B é o mesmo que A interseção com B (elementos que aparecem em ambos).
C = A.intersection(B)
print(C)

C = A & C
print(C)

# Resultado:
# {0, 9}
# {0, 9}
# -----------------------------------------------------------------------------

'''
Símbolo matemático | Operador Python | Descrição
----------------------------------------------------------------------
E ∈ S              | in              | elemento E é membro de S
A ⊆ B              | <=              | A é um subconjunto de B
A ⊂ B              | <               | A é um subconjunto próprio de B
A ∪ B              | |               | A união com B
A ∩ B              | &               | A interseção com B
A ∖ B              | -               | diferença entre A e B
'''

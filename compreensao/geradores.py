# A compreensão de geradores (generator) tem a mesma sintaxe da Lista,
# o que muda é que no lugar de [] usmaos () .
# A vantagem de usar Gerador é que ele não cria todos os valores, ele
# vai criando conforme você vai iterando sobre le.
# Dependendo do tamanho do arquivo é uma ótima opção.


generator = (n for n in range(1, 7) if n % 2 == 0)

valor = next(generator)
print(valor)

valor = next(generator)
print(valor)

valor = next(generator)
print(valor)

# Resultado:
# 2
# 4
# 6
# --------------------------------------------------------------------------

generator = (n for n in range(1, 7) if n % 2 != 0)

for n in generator:
    print(n)

# Resultado:
# 1
# 3
# 5

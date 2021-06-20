inteiro = 3  # int

flutuante = 6.9648  # float

print(type(inteiro), type(flutuante))

# Resultado:
# int float
# -----------------------------------------------------------------------------

arredondar_sem_casa_decimal = round(flutuante)

# Resultado:
# 7
# -----------------------------------------------------------------------------

arredondar_com_casa_decimal = round(flutuante, ndigits=2)

# Resultado:
# 6.96
# -----------------------------------------------------------------------------

# Para formatar um número usamos interpolação... Acaba que também arredonda.
formatar_numero = f'{flutuante:.2f}'

# Resultado:
# 9.96
# -----------------------------------------------------------------------------

# Operação entre inteiro e flutuante resultará em flutuante
resultado = 6.0 / 3

# Resultado:
# 2.0
# -----------------------------------------------------------------------------

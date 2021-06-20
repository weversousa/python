try:
    valor = 7 / 0
except ZeroDivisionError as e:
    print(f"{e}: Não é possível realizar divisão por ZERO!")
else:
    # Não é necessário fazer no ELSE, pode fazer tudo no TRY
    print(f"O resultado é {valor}")
finally:
    print("Eu sempre serei executado, mesmo se cair no erro.")


# Podemor encadear vários EXCEPT
try:
    ...
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)


# Podemos fazer assim também
try:
    ...
except (ZeroDivisionError, TypeError) as e:
    print(e)

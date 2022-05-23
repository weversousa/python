# Operadores lógicos

Os operadores lógicos são usados para unir duas ou mais expressões condicionais. Isso é feito por meio de conectivos.

## e

Retorna True se todas as condições forem verdadeiras, caso contrário retorna False.

*Exemplo*:
~~~python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
~~~

*Saída*:
~~~python
True
False
False
False
~~~

## ou

Retorna True se uma das condições for verdadeiras, caso contrário retorna False.

*Exemplo*:
~~~python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
~~~

*Saída*:
~~~python
True
True
True
False
~~~

## negação

Inverte o resultado: se o resultado da expressão for True, o operador retorna false.

*Exemplo*:
~~~python
print(not True)
print(not False)
~~~

*Saída*:
~~~python
False
True
~~~

## Dupla negação

Inverte o resultado do not: se o resultado da expressão for True, o operador retorna false.

*Exemplo*:
~~~python
print(not not True)
print(not not False)
~~~

*Saída*:
~~~python
True
False
~~~
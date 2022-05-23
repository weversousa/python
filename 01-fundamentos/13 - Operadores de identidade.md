# Operadores de identidade

Os operadores de identidade servem para a comparação de objetos. Nessa comparação é verificado se eles ocupam a mesma posição na memória, o que significará que se trata do mesmo objeto.

Quando declaramos uma string no Python, o seu valor é guardado num local especial da memória. Assim, quando usamos esse valor repetidas vezes, o Python pode utilizar o mesmo objeto em cada uma delas.

## é

*Exemplo*:
~~~python
nome_1, nome_2, nome_3 = 'Ana', 'ana', 'Ana'

print(nome_1 is nome_3)
print(nome_1 is nome_2)
~~~

*Saída*:
~~~python
True
False
~~~

## não é

*Exemplo*:
~~~python
nome_1, nome_2, nome_3 = 'Ana', 'ana', 'Ana'

print(nome_1 is not nome_3)
print(nome_1 is not nome_2)
~~~

*Saída*:
~~~python
False
True
~~~
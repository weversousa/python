# Recursividade

Uma função recursiva, chama a si até o parâmetro atingir a condição desejada.

*Exemplo*:
~~~python
def funcao(numero):

    if numero > 5:
        print('Encerrado!!!!!')

    else:
        print(f'O numero está valendo {numero}')
        return funcao(numero + 1)


funcao(1)
~~~

*Saída*:
~~~python
O numero está valendo 1
O numero está valendo 2
O numero está valendo 3
O numero está valendo 4
O numero está valendo 5
Encerrado!!!!!
~~~
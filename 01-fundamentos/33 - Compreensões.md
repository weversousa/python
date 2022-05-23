# Compreensões

## Compreensão de Lista

*Exemplo*:
~~~python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
~~~

*Saída*:
~~~python
[2, 4, 6, 8, 10]
~~~

*Exemplo*:
~~~python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
impares = [numero for lista in matriz for numero in lista if numero % 2 != 0]
print(impares)
~~~

*Saída*:
~~~python
[1, 3, 5, 7, 9]
~~~

## Compreensão de Dicionário

*Exemplo*:
~~~python
frutas = [('maça', 2.90), ('uva', 7.90), ('mamao', 5.90), ('pera', 4.43)]

qtde = 2

total = {fruta[0]: fruta[1] * qtde for fruta in frutas if fruta[0] != 'uva'}
print(total)
~~~

*Saída*:
~~~python
{'maça': 5.8, 'mamao': 11.8, 'pera': 8.86}
~~~

## Compreensão de Gerador

* Não carrega todo o arquivo para a memória conforme os demais
* Gera cada valor ao ser chamado o próximo valor
* Ótimo para arquivos grandes

*Exemplo*:
~~~python
gerador = (n for n in range(1, 7) if n % 2 == 0)

print(next(gerador))
print(next(gerador))
print(next(gerador))
~~~

*Saída*:
~~~python
2
4
6
~~~

*Exemplo*:
~~~python
gerador = (n for n in range(1, 7) if n % 2 != 0)

for n in gerador:
    print(n)
~~~

*Saída*:
~~~python
1
3
5
~~~
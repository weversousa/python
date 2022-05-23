# Tipo decimal

O tipo decimal (float) é composto por caracteres numéricos reais (positivos ou negativos).

*Exemplo*:
~~~python
print(type(7.3))
print(type(-4.9))
~~~

*Saída*:
~~~python
<class 'float'>
<class 'float'>
~~~

## Classe float

A classe `float` é uma classe interna e através dela é possível converter texto e número inteiro em número decimal.  

No caso do texto precisa ser uma sequência de caracteres que representa um número decimal, espaços em branco no início e/ou no fim da sequência de caracteres são removidos automaticamente, diferente disso o programa retorna uma excessão.

*Exemplo*:
~~~python
print(type('11.5937'))

print(type(float('11.5937')))
print(type(float('  11.5937  ')))

print(type(float('11')))
print(float('11'))

print(type(float('11. 5937')))
print(type(float('11.5937b')))
~~~

*Saída*:
~~~python
<class 'str'>

<class 'float'>
<class 'float'>

<class 'float'>
11.0

ValueError
ValueError
~~~

## Função round

O método `round` é um método nativo que recebe um número decimal e a quantidade de casas decimais (opcional) e retorna o número arredondado com base nessas informações. Se não especificado a quantidade de casas decimais o valor é arredondado para o primeiro número inteiro mais próximo.

*Exemplo*:
~~~python
print(round(1.2837382038, 2))
print(round(1.2837382038, 1))
print(round(1.6))
print(round(1.5))
print(round(1.4))
~~~

*Saída*:
~~~python
1.28
1.3
2
2
1
~~~
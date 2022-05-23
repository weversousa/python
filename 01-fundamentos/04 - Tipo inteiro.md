# Tipo inteiro

O tipo inteiro (int) é composto por caracteres numéricos reais (positivos ou negativos).

*Exemplo*:
~~~python
print(type(7))
print(type(-4))
~~~

*Saída*:
~~~python
<class 'int'>
<class 'int'>
~~~

## Classe int

A classe `int` é uma classe nativa e através dela é possível converter texto e número decimal em número inteiro.

No caso do texto precisa ser uma sequência de caracteres que representa um número real, espaços em branco no início e/ou no fim da sequência de caracteres são removidos automaticamente, diferente disso o programa retorna uma excessão, um número decimal em forma de texto não é válido.

*Exemplo*:
~~~python
print(type('11'))

print(type(int('11')))
print(type(int('  11  ')))

print(type(int('1 1')))
print(type(int('11b')))
print(type(int('11.55')))
~~~

*Saída*:
~~~python
<class 'str'>

<class 'int'>
<class 'int'>

ValueError
ValueError
ValueError
~~~

No caso de um número decimal a classe `int` retorna somente a parte inteira do valor.

*Exemplo*:
~~~python
print(type(8.3692))

print(type(int(8.3692)))
print(int(8.3692))
~~~

*Saída*:
~~~python
<class 'float'>

<class 'int'>
8
~~~

## Função abs

O método `abs` é um método nativo que recebe um número negativo real ou decimal e retorna o mesmo número positivo.

*Exemplo*:
~~~python
print(abs(-4))
print(abs(-13.96))
~~~

*Saída*:
~~~python
4
13.96
~~~
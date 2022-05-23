# Os operadores de atribuição

Os operadores de atribuição atribuem valor a uma variável.

## =

*Exemplo*:
~~~python
x = 1
~~~

## +=

Equivalente a: `x = x + 1`.

*Exemplo*:
~~~python
x += 1
~~~

## -=

Equivalente a: `x = x - 1`.

*Exemplo*:
~~~python
x -= 1
~~~

## *=

Equivalente a: `x = x * 1`.

*Exemplo*:
~~~python
x *= 1
~~~

## /=

Equivalente a: `x = x / 1`.

*Exemplo*:
~~~python
x /= 1
~~~

## //=

Equivalente a: `x = x // 1`.

*Exemplo*:
~~~python
x //= 1
~~~

## %=

Equivalente a: `x = x % 1`.

*Exemplo*:
~~~python
x %= 1
~~~

## **=

Equivalente a: `x = x ** 1`.

*Exemplo*:
~~~python
x **= 1
~~~

### Palavra reservada del

Quando um valor é atribuido a uma variável, pode se dizer que uma variável foi "definida."

E é possível remover essa definição, deletar um valor de uma variável removendo esse valor da memória, desfazendo a declaração da variável. Para isso usamos a palavra reservada `del`.

Feito isso, ao tentar acessar uma declara não definida o programa retorna-rá um erro.

*Exemplo*:
~~~python
brinquedo = 'bola'
print(brinquedo)

del brinquedo
print(brinquedo)
~~~

*Saída*:
~~~python
bola

NameError: name 'brinquedo' is not defined
~~~
# Tipo lógico

O tipo lógico (bool) é composto pelos caracteres **Verdadeiro** ou **Falso**.

*Exemplo*:
~~~python
print(type(True))
print(type(False))
~~~

*Saída*:
~~~python
<class 'bool'>
<class 'bool'>
~~~

## Classe bool

A classe `bool` é uma classe nativa e através dela é possível converter qualquer caractere em um valor lógico.

Podemos converter Estruturas de Dados (Tupla, Lista, Dicionário), int, string, None em verdadeiro ou falso.

Porém é bom saber o que cada valor vai retornar.

Por exemplo, uma lista vazia `[]` é False, já um lista não vazia `['uva']` é True.
Assim como uma string vazia `''` é False, já uma string com um simples espaço `' '` é True.
O número zero é False, qualquer outro número **positivo/negativo** é True.

### False

*Exemplo*:
~~~python
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
~~~

*Saída*:
~~~python
False
False
False
False
False
False
~~~

### True

*Exemplo*:
~~~python
print(bool(1))
print(bool(' '))
print(bool('a'))
print(bool(['ovo']))
print(bool(('arros', 'manteiga')))
print(bool({'nome': 'Maria'}))
~~~

*Saída*:
~~~python
True
True
True
True
True
True
~~~

## Negação

A negação em Python é representada pela palavra reservada `not`, e retorna um valor **bool**.

A negação **inverte** o valor Boolean de um dado, vimos acima que zero convertido para bool resulta em False, então `not 0` resulta em True.

Outro conceito existente é o da dupla nagação `not not`, que serve para devolver o valor bool original.

Resumindo, a dupla negação vai negar a negação rsrsrsrrsrs...

*Exemplo*:
~~~python
print(bool(0))

print(not 0)

print(not not 0)
~~~

*Saída*:
~~~python
False
True
False
~~~

Então quando quiser saber o valor lógico de um dado sem usar a classe `bool` é só usar `not not`.

## Função all

O método `all` é nativo e recebe lista de elementos de qualquer tipo, e retorna `True` se todos forem verdade, caso contrário retorna `False`.

*Exemplo*:
~~~python
print(all([1, ' ']))
print(all([0, '', True]))
~~~

*Saída*:
~~~python
True
False
~~~
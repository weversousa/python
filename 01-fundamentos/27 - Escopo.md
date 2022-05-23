# Escopo

Tudo que está fora de **estruturas** está no `escopo global`do programa. Já o que estiver dentro de alguma estrutura de repetição, condição, função e etc... faz parte do `escopo local`.

Sendo asism são locais diferentes, por isso podemos ter variáveis de mesmo nome em cada escopo com valores diferentes.


No caso abaixo **n** ainda valerá 10 pois a função tem um **n** diferente do que está fora. E como o `print` está sendo executad fora da função, ele vai usar o **n** de fora que é o **global**.

*Exemplo*:
~~~python
n = 10


def funcao():
    n = 55


funcao()

print(n)
~~~

*Saída*:
~~~python
10
~~~

Já no caso abaixo **n** valerá 55 pois a palavrada reservada `global` faz com que a variável `n` usada dentro do escopo da função seja o **n** que está no escopo global, sendo assim dentro da função nós conseguimos alterar o valor do **n** que está do lado de fora dela.

*Exemplo*:
~~~python
n = 10


def funcao():
    global n
    n = 55


funcao()

print(n)
~~~

*Saída*:
~~~python
55
~~~
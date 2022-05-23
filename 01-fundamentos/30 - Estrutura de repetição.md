## Para

A estrutura de repetição para (for) serve para percorrer um iterável.
Assim podemos tratar cada item.

*Exemplo*:
~~~python
for fruta in ['banana', 'uva', 'jaca']:
    print(fruta)

for letra in 'Ana':
    print(letra)
~~~

*Saída*:
~~~python
banana
uva
jaca

A
n
a
~~~

A classe `enumerate` é nativa e podemos usá-la para numerar os itens.
Por padrão é iniciado com 0, mas podemos passar o valor inicial da numeração.

*Exemplo*:
~~~python
for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"]):
    print(indice, curso)

for indice, curso in enumerate(["Python", "Java", "HTML", "PHP"], start=1):
    print(indice, curso)
~~~

*Saída*:
~~~python
0 Python
1 Java
2 HTML
3 PHP

1 Python
2 Java
3 HTML
4 PHP
~~~

A classe `range` é nativa e podemos usá-la para criar uma contagem.
Essa classe pode receber até 3 parâmetros, iniciar, parar, etapa.

Se passado somente 1, será considerado como valor de parada e iniciado em 0 e pulando de 1 em 1, e ele não vai até o valor de parada nunca é sempre até o valor antes dele.

Se passados 2 parâmetros, será considerado como valor inicial e valor de parada.

O terceiro parâmetro sempre será o etapa e é quem decide de quantas em quantas casas pular.

*Exemplo*:
~~~python
for n in range(3):
    print(n)

for n in range(1, 3):
    print(n)

for n in range(2, 11, 2):
    print(n)
~~~

*Saída*:
~~~python
0
1
2

1
2

2
4
6
8
10
~~~

*Exemplo*:
~~~python
for n in range(3, 0, -1):
    print(n)
~~~

*Saída*:
~~~python
3
2
1
~~~

A palavra reservada `continue` faz com que o valor seja pulado, e não exibido.

*Exemplo*:
~~~python
for letra in ['a', 'c', 'a', 'b', 'd', 'a']:
    if letra == 'a':
        continue
    print(letra)
~~~

*Saída*:
~~~python
c
b
d
~~~

A palavra reservada `break` encerra o laço de repetição assim que encontrar o valor.

*Exemplo*:
~~~python
for letra in ['a', 'c', 'a', 'b', 'd', 'a']:
    if letra == 'b':
        break
    print(letra)
~~~

*Saída*:
~~~python
a
c
a
~~~

## Quando

A estrutura de repetição quando (while) serve para repetir uma determinada ação.
Normalmente usada quando não sabemos a quantidade de repetição necessária.


Enquanto a variável "c" for menor que 4 ela será exibida.
NÃO pode esquecer de mudar o valor da variável "c" a cada repetição caso contrário o loop nunca vai terminar.

~~~python
c = 1

while c < 4:
    print(c)
    c += 1
~~~

*Saída*:
~~~python
1
2
3
~~~

Esse loop só será encerrado quando o usuário digitar a letra "s".

*Exemplo*:
~~~python
while True:
    entrada = input("Deseja sair? [s/n]")
    if entrada.strip().lower() == "s":
        break
~~~
# Tipo texto

O tipo texto (string) é composto por qualquer sequência de caracteres envolvidos entre `''` ou `""`.

Sobre a string:
* imutável
* indexada

*Exemplo*:
~~~python
print(type('Weverton Teixeira'))
print(type("Weverton Teixeira"))
~~~

*Saída*:
~~~python
<class 'str'>
<class 'str'>
~~~

Mesmo que não tenha caractere, ao usar as aspas é declarado uma string.

*Exemplo*:
~~~python
print(type(''))
print(type(' '))
~~~

*Saída*:
~~~python
<class 'str'>
<class 'str'>
~~~

## Classe str

A classe `str` é uma classe interna e através dela é possível converter qualquer caractere em texto. E por ser uma classe possui métodos para modificar a string.

*Exemplo*:
~~~python
print(str(2))
print(str(7.30))
print(str(()))
print(str([]))
print(str({}))
~~~

*Saída*:
~~~python
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
~~~

### Função uper

O método `uper` pertence à classe str e transforma todos os caracteres em letras maiúsculas.

*Exemplo*:
~~~python
print('sp'.upper())
~~~

*Saída*:
~~~python
SP
~~~

### Função lower

O método `lower` pertence à classe str e transforma todos os caracteres em letras minúsculas.

Exemplo
~~~python
print('BA'.lower())
~~~

*Saída*:
~~~python
ba
~~~

### Função capitalize

O método `capitalize` pertence à classe str e transforma a primeira letra em Maiúscula.

Exemplo
~~~python
print('weverton'.capitalize())
~~~

*Saída*:
~~~python
Weverton
~~~

### Função find

O método `find` pertence à classe str e retorna o índice em que começa o valor procurado.
Cada caractere refere-se a um ídicide, iniciado por zero.

string --> 'uva roxa'
Ídice  -->  01234567

Perceba que o espaço também é considerado na contagem.

Vamos descobrir em qual índice começa a palavra "dia" na string "Bom dia!".

*Exemplo*:
~~~python
print('Bom dia!'.find('dia'))
~~~

*Saída*:
~~~python
4
~~~

Caso seja somente 1 caractere, é retornado o valor exato do índice dele.
Caso tenha mais de 1 caractere igual ao especificado é retornado o primeiro.

*Exemplo*:
~~~python
print('Ana'.find('n'))
~~~

*Saída*:
~~~python
1
~~~

### Função split

O método `split` pertence à classe str e transforma a string em uma **Lista**.
Pode ou não ser passado argumento a esse método, caso não seja passado um argumento os espaços entre cada palavra vai servir como delimitador e então cada palavra será um elemento da lista.

Vamos aplicar esse método em uma string com 3 frutas separadas por **espaço**.

*Exemplo*:
~~~python
print('uva maça pêra'.split())
~~~

*Saída*:
~~~python
['uva', 'maça', 'pêra']
~~~

Mas também é possível específicar o que está separando os elementos.

Vamos aplicar esse método em uma string com 3 cores separadas por **;**.

*Exemplo*:
~~~python
print('azul;verde;marrom'.split(';'))
~~~

*Saída*:
~~~python
['azul', 'verde', 'marrom']
~~~

### Função replace

O método `replace` pertence à classe str e substitui um valor por outro dentro da string.
Todos os valores iguais são substituídos

*Exemplo*:
~~~python
print('A minha cor favorita é azul.'.replace('azul', 'vermelha'))
~~~

*Saída*:
~~~python
A minha cor favorita é vermelha.
~~~

### Funções lstrip, rstrip e strip

Todos as 3 funções pertencem à classe str.
O método `lstrip` recebe um argumento e remove o valor da string se ele estiver no início.
O método `rstrip` recebe um argumento e remove o valor da string se ele estiver no fim.
O método `strip` recebe um argumento e remove o valor da string se ele estiver no início e no fim.

*Exemplo*:
~~~python
print('amora'.lstrip('a'))
print('amora'.rstrip('a'))
print('amora'.strip('a'))

print('mmmMárcia'.lstrip('m'))
~~~

*Saída*:
~~~python
mora
amor
mor

Márcia
~~~

Se não for informado o valor a ser removido o método removerá espaços em branco.

*Exemplo*:
~~~python
print('  amora  ')
print('  amora  '.strip())
~~~

*Saída*:
~~~python
  amora  
amora
~~~

## Indexação

Vimos que uma string é indexada, cada caractere contém o seu índice iniciado em zero, sendo assim podemos acessar cada caractere por seu índice utilizando `[]`.

*Exemplo*:
~~~python
print('AEIOU'[0])
print('AEIOU'[1])
print('AEIOU'[2])
print('AEIOU'[3])
print('AEIOU'[4])
~~~

*Saída*:
~~~python
A
E
I
O
U
~~~

Porém muita atenção ao usar esse procedimento, caso o índice não exista é retornado um erro ao seu programa e ele vai parar de ser executado.

*Exemplo*:
~~~python
print('AEIOU'[5])
~~~

*Saída*:
~~~python
IndexError
~~~

## Multiplicar texto

É possível multiplicar a String.

*Exemplo*:
~~~python
print('!' * 5)
~~~

*Saída*:
~~~python
!!!!!
~~~
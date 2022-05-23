# Formatação de texto

Existem 4 formas de concatenar valores para formar um texto, são elas:
* Usando o sinal de `%`
    * `%s` String
    * `%d` Int
    * `%f` Float
* Com o método `format` da classe da String
* Usando o sinal de `+` entre as Strings
* E o mais moderno `fstring`

*Exemplo*:
~~~python
nome, idade, peso = 'Weverton', 31, 61.35

formatacao = '%s %d %f'
print(formatacao % (nome, idade, peso))
print('%s %d %f' % (nome, idade, peso))

formatacao = '{} {} {}'
print(formatacao.format(nome, idade, peso))
print('{} {} {}'.format(nome, idade, peso))

print(nome + ' ' + str(idade) + ' ' + str(peso))

print(f'{nome} {idade} {peso}')
~~~

*Saída*:
~~~python
Weverton 31 61.350000
Weverton 31 61.350000

Weverton 31 61.35
Weverton 31 61.35

Weverton 31 61.35

Weverton 31 61.35
~~~



## F-strings

A `f-strings` (strings literais formatadas), são strings com a letra `f` no início e chaves `{}` para realizar a interpolação de expressões.

### Trabalhando com números

Para definir um separador de milhar existem somente 2 opções:
* `,` padrão americano e oficial da linguagem Python
* `_` que também é permitido pela linguagem Python

~~~python
valor = 100000000000
print(f'{valor:,}')
print(f'{valor:_}')
~~~

*Saída*:
~~~python
100,000,000,000
100_000_000_000
~~~

No Brasil o separador de milhar é o `.` então temos um jeito de adaptar isso.

~~~python
valor = 100000000000
print(f'{valor:_}'.replace('_', '.'))
~~~

*Saída*:
~~~python
100.000.000.000
~~~

Dica!
Como formatar um valor grande para o padrão de moeda brasileiro.

~~~python
ferrari_preco = 1340599.678293
print(f'R$ {ferrari_preco:_.2f}'.replace('.', ',').replace('_', '.'))
~~~

*Saída*:
~~~python
R$ 1.340.599,68
~~~

Para definir a quantidade de casas decimais.
Se o valor após o `.` for 0, arredonda para o inteiro mais próximo.
O `f` representa **float**.

~~~python
print(f'{9.8268:.2f}')
print(f'{9.8268:.1f}')
print(f'{9.8268:.0f}')
print(f'{9.3268:.0f}')
~~~

*Saída*:
~~~python
9.83
9.8
10
9
~~~

Converter para um valor em porcentagem.
O `%` significa: multiplica o valor por 100 e inclui o `%` ao final

~~~python
produtos_defeito = 295
produtos_reparados = 126

reparo_em_porcentagem = produtos_reparados / produtos_defeito

print(f'{reparo_em_porcentagem:%}')
print(f'{reparo_em_porcentagem:.2%}')
~~~

*Saída*:
~~~python
42.711864%
42.71%
~~~

Podemos especificar um tamanho para uma String e se o tamanho do valor da  
String não atender o valor especificado, podemos preencher com um caractere os  
espaços faltate para atender o tamanho que queremos a nossa String.  

Vamos supor que uma variável receba o valor `23`, o tamanho dessa String é de 2.  
Porém queremos que ela tenha um tamanho de 10, então precisamos de 8 caracteres  
a mais nessa String.  

E ai que vem o mais legal, existem três formas de se fazer isso, são elas:
* `^` o valor original ficará ao centro e o valor de preenchimento ao seu redor
* `>` o valor original ficará à direita do valor de preenchimento
* `<` o valor original ficará à esquerda do valor de preenchimento

À esquerda dos sinais acima fica o caractere de preenchimento e à sua direita o  
tamanho final da String

Obs: Se o valor da String já tiver o tamanho desejado nada acontece.

~~~python
n = 23

exemplo_1 = f'{n:0>10}'
print(exemplo_1)

exemplo_2 = f'{n:0<10}'
print(exemplo_2)

exemplo_3 = f'{n:a^10}'
print(exemplo_3)
~~~

*Saída*:
~~~python
0000000023
2300000000
aaaa23aaaa
~~~

Um exemplo de uso, seria padronizar uma exibição de forma alinhada.

~~~python
fruta_1, fruta_2, fruta_3 = 'Banaba', 'Maçã', 'Uva'

exibir = f'{fruta_1} R$ 2,50\n{fruta_2} R$ 5,50\n{fruta_3} R$ 7,50'
print(exibir)

exibir = f'{fruta_1: <10} R$ 2,50\n{fruta_2: <10} R$ 5,50\n{fruta_3: <10} R$ 7,50'
print(exibir)
~~~

*Saída*:
~~~python
Banaba R$ 2,50
Maçã R$ 5,50
Uva R$ 7,50

Banaba     R$ 2,50
Maçã       R$ 5,50
Uva        R$ 7,50
~~~
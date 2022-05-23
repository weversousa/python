# Entrada e Saída

I/O

## Impressão

O método `print` que já usamos diversas as vezes é um método de saída de dados, ele exibe informações no terminal do computador.

*Exemplo*:
~~~python
print('Olá mundo!')
~~~

*Saída*:
~~~python
Olá mundo!
~~~

## Entrada

O método `input` lê a entrada que o usuário digitou. O retorno da função input sempre será do tipo texto.

*Exemplo*:
~~~python
dia = input('Digite o dia do seu aniversário: ')
mes = input('Digite o mês do seu aniversário: ')
ano = input('Digite o ano do seu aniversário: ')

print(dia, mes, ano, sep='/', end='.')
~~~

*Saída*:
vídeo

## argv

É um atributo que pertence a bibliotéca `sys` não é nativa porém já vem instalada e para usá-la é só importar.

Esse atributo é uma lista que armazena todos os valores colocados na frente do comando para executar o programa.

Exemplo: `python main.py item1 item2 item3`

Cada item separado por espaços será um item na lista armazanada em `argv`

*Exemplo*:
~~~python
from sys import argv


print(argv)
~~~

*Saída*:
vídeo

## Função open

O método `open` é nativo e é usado para abrir/criar arquivos de diversos tipos de extensões, `.txt`, `.json` e etc...

Esse método retorna um objeto do tipo `TextIOWrapper`, e esse objeto contém métodos para trabalhar com o arquivo.

**Importante!**
Sempre que abrir um arquivo é necessário fechá-lo após o uso.
Caso contrário vai ficar ocpando memória e se for um arquivo grande vai impactar muito no desmepenho do programa.

*Exemplo*:
~~~python
arquivo = open(file='.txt', mode='w', encoding='utf-8')
print(arquivo)
arquivo.close()
~~~

*Saída*:
~~~python
<_io.TextIOWrapper name='.txt' mode='w' encoding='utf-8'>
~~~

### Atributo writelines

Esse atributo é uma função que recebe um iterável e vai escrever cada item do iterável dentro do arquivo aberto.

*Exemplo*:
~~~python
produtos = ['produto,preço,qtde\n', 'arroz,24.50,3\n', 'café,13.99,2\n']

arquivo = open(file='.txt', mode='w', encoding='utf-8')
arquivo.writelines(produtos)
arquivo.close()
~~~

*Saída*:
~~~python
# Arquivo .txt

produto,preço,qtde
arroz,24.50,3
café,13.99,2
~~~

### Atributo write

Esse atributo é uma função vai escrever dentro do arquivo aberto.

*Exemplo*:
~~~python
arquivo = open(file='.txt', mode='w', encoding='utf-8')

arquivo.write('produto,preço,qtde\n')
arquivo.write('ovo,16.00,1\n')
arquivo.write('feijão,7.99,3\n')

arquivo.close()
~~~

*Saída*:
~~~python
# Arquivo .txt

produto,preço,qtde
ovo,16.00,1
feijão,7.99,3
~~~

### Atributo read

Esse atributo é uma função que vai ler de uma vez as informações e retornar em um único texto.

*Exemplo*:
~~~python
arquivo = open(file='.txt', mode='r', encoding='utf-8')
print(arquivo.read())
arquivo.close()
~~~

*Saída*:
~~~python
produto,preço,qtde
ovo,16.00,1
feijão,7.99,3

~~~

esse método também aceita um parâmetro, que é um valor inteiro que representa a quantidade de caracteres que deseja retornar.

E em quanto você não fechar o arquivo, ao ser chamado novamente o método ele vai dar sequência na ordem dos caracteres.

*Exemplo*:
~~~python
arquivo = open(file='.txt', mode='r', encoding='utf-8')

print(arquivo.read(3))
print(arquivo.read(4))

arquivo.close()
~~~

*Saída*:
~~~python
pro
duto
~~~

### Atributo readlines

Esse método lê todo o arquivo e armazena em uma lista, onde cada linha torna-se um item da lista.


*Exemplo*:
~~~python
arquivo = open(file='.txt', mode='r', encoding='utf-8')
print(arquivo.readlines())
arquivo.close()
~~~

*Saída*:
~~~python
['produto,preço,qtde\n', 'ovo,16.00,1\n', 'feijão,7.99,3\n']
~~~

## Estrutura with

Com essa estrutra não é necessário fechar o arquivo, não corre o risco de esquecer de fechar o arquivo e ele ficar ocupando memória. Ao sair da estrutura o aqruivo é fechad automaticamente.

*Exemplo*:
~~~python
with open(file='.txt', mode='r', encoding='utf-8') as arquivo:
    print(arquivo.readlines())
~~~

*Saída*:
~~~python
['produto,preço,qtde\n', 'ovo,16.00,1\n', 'feijão,7.99,3\n']
~~~
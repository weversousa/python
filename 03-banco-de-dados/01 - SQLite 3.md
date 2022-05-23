# SQLite 3

Em Python o `SQLite` faz partes das bibliotecas que já vem instaladas com a linguagem, então basta importá-la.

*Exemplo*:
~~~python
import sqlite3


# Cria uma conexão com o banco, se o banco não existir será criado
with sqlite3.connect('caminho/banco') as conexao:

    # Função que retorna as funções para interagir com o banco de dados
    cursor = conexao.cursor()

    # Comandos SQL em formato de texto
    cursor.execute("comandos SQL")

    # Caso a ação seja, inserir, alterar ou deletar registros de uma tabela
    cursor.commit()


    """ Caso o comando SQL seja uma consulta """

    # Retorna todos os registros de uma vez em uma lista de tuplas
    cursor.fetchall()

    # Retorna uma tupla por vez a cada chamada
    cursor.fetchone()

    # Retorna a quantidade de registros de uma vez em uma lista de tuplas
    cursor.fetchmany(size)

    # Nunca esquecer de encerrar o cursor
    cursor.close()
~~~

## Chave Estrangeira

O SQLite não tem a funcionalidade de `Chave estrangeria` ativada. Para isso é necessário ativá-la.
Se o valor for 0 está OFF, já se for 1 está ON.

*Exemplo*:
~~~python
import sqlite3


with sqlite3.connect('teste.db') as conexao:
    cursor = conexao.cursor()

    print(cursor.execute('PRAGMA Foreign_keys;').fetchone())

    cursor.execute('PRAGMA Foreign_keys = ON;')

    print(cursor.execute('PRAGMA Foreign_keys;').fetchall())

    cursor.close()
~~~

*Saída*:
~~~python
(0,)
[(1,)]
~~~

## Dica!

Pegar nomes das colunas.

*Exemplo*:
~~~python
import sqlite3


with sqlite3.connect('#') as conexao:
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM nome_da_tabela;')
    colunas = [coluna[0] for coluna in cursor.description]
    print(colunas)

    cursor.close()
~~~

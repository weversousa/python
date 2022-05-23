# SQL Server

Em Python o `SQL Server` não é nativo, é necessário instalar a biblioteca `pip install pyodbc` e importá-la.

Para acessar um servidor local, o parâmetro **server** ficaria `server=r'localhost\SQLEXPRESS'` e se não tiver colocado senha para acesso pode omitir os parâmetros **uid** e **pwd**.

*Exemplo*:
~~~python
import pyodbc


with pyodbc.connect(driver='{SQL Server}', server='', database='', uid='', pwd='') as conexao:
    with conexao.cursor() as cursor:
        pass  # As demais funcionalidades seguir o tutorial do SQLite 3


# Outra forma de passar os parâmetros para conexão
with psycopg2.connect('Driver={SQL Server};Server=#;Database=#;UID=#;PWD=#') as conexao:
    with conexao.cursor() as cursor:
        pass
~~~

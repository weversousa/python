# Postgres SQL

Em Python o `Postgres SQL` não é nativo, é necessário instalar a biblioteca `pip install psycopg2-binary` e importá-la.

Por padrão o host é localhost e a porta é 5432, e ambos podem ser omitidos.

*Exemplo*:
~~~python
import psycopg2


# Cria uma conexão com o banco
with psycopg2.connect(database='', user='', password='', host='', port='') as conexao:
    with conexao.cursor() as cursor:
        pass  # As demais funcionalidades seguir o tutorial do SQLite 3


# Outra forma de passar os parâmetros para conexão
with psycopg2.connect(f'postgresql://usuário:senha@host:porta/banco') as conexao:
    with conexao.cursor() as cursor:
        pass
~~~


## Dica!

Criando uma classe para interagir com o banco de dados. Ela vai cuidar da conexão e também da manipulação dos dados.

*Exemplo*:
~~~python
class Conexao:

    def __init__(self, m_host, db, usr, pwd):
        self._conectar = psycopg2.connect(host=m_host, database=db, user=usr, password=pwd)

    def manipular(self, sql):
        try:
            cursor = self._conectar.cursor()
            cursor.execute(sql)
            cursor.close()
            conectar.commit()
        except:
            return False

    def consultar(self, sql):
        try:
            cursor = self._conectar.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return False
        finally:
            cursor.close()

    def fechar(self):
        self._conectar.close()
~~~
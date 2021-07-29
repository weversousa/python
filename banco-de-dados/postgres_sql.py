import psycopg2


connection = psycopg2.connect(
    host='localhost',
    database='regiao',
    user='postgres',
    password='abobrinha'
)

cursor = connection.cursor()
# -----------------------------------------------------------------------------

sql = '''
CREATE TABLE IF NOT EXISTS cidade(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    uf CHAR(2)
);'''

cursor.execute(sql)
connection.commit()
# -----------------------------------------------------------------------------

sql = """
INSERT INTO cidade
VALUES (default, 'São Paulo', 'SP'),
       (default, 'Rio de Janeiro', 'RJ');"""

cursor.execute(sql)
connection.commit()
# -----------------------------------------------------------------------------

sql = 'SELECT * FROM cidade;'

cursor.execute(sql)

cidades = cursor.fetchall()
for cidade in cidades:
    print(cidade)

# (1, 'São Paulo', 'SP')
# (2, 'Rio de Janeiro', 'RJ')
# -----------------------------------------------------------------------------

cursor.close()
connection.close()
# -----------------------------------------------------------------------------


class Conexao:
    def __init__(self, m_host, db, usr, pwd):
        self._connection = psycopg2.connect(
            host=m_host,
            database=db,
            user=usr,
            password=pwd
        )

    def manipular(self, sql):
        try:
            cursor = self._connection.cursor()
            cursor.execute(sql)
            cursor.close()
            connection.commit()
        except:
            return False

    def consultar(self, sql):
        try:
            cursor = self._connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return False
        finally:
            cursor.close()

    def fechar(self):
        self._connection.close()


con = Conexao('localhost', 'regiao', 'postgres', 'abobrinha')

sql = "INSERT INTO cidade VALUES (default, 'Minas Gerais', 'MG')"

if con.manipular(sql):
    print('Valores inseridos com sucesso.')


sql = 'SELECT * FROM cidade;'

cidades = con.consultar(sql)

for cidade in cidades:
    print(cidade)

# (1, 'São Paulo', 'SP')
# (2, 'Rio de Janeiro', 'RJ')
# (3, 'Minas Gerais', 'MG')

con.fechar()
# -----------------------------------------------------------------------------

import postgresql

db = postgresql.open('pq://postgres:abobrinha@localhost/regiao')

sql = """
INSERT INTO cidade
VALUES (default,'Curitiba,'PR')"""

try:
    db.execute(sql)
except:
    print("erro")
finally:
    db.close()

import pyodbc


connection = pyodbc.connect(
    driver='{SQL Server}',
    server=r'localhost\SQLEXPRESS',
    database='estudos'
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM nome_da_tabela')

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()


cursor.close()
connection.close()


# -----------------------------------------------------------------------------

# Acessar um servidor externo

connection = pyodbc.connect(
    'Driver=SQL Server;'
    'Server={};'
    'Database={};'
    'UID={};'
    'PWD={}'
)

connection = pyodbc.connect(
    driver='SQL Server',
    server='{}',
    database='{}',
    uid='{}',
    pwd='{}'
)

import pyodbc


connection = pyodbc.connect(
    driver='{SQL Server}',
    server=r'localhost\SQLEXPRESS',
    database='estudos'
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM filho')

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()


cursor.close()
connection.close()


# -----------------------------------------------------------------------------

# Acessar um servidor externo

connection = pyodbc.connect(
    driver='#',
    server='#',
    database='#',
    uid='#',
    pwd='#'
)

# -----------------------------------------------------------------------------

# Outra forma de passar o parãmetro da conexão e de manipular a conn e cursor

with pyodbc.connect('Driver=#;Server=#;Database=#') as connection:
    with connection.cursor() as cursor:
        ...

with pyodbc.connect('Driver=#;Server=#;Database=#;UID=#;PWD=#') as connection:
    with connection.cursor() as cursor:
        ...

# -----------------------------------------------------------------------------

# Pegar nomes das colunas

with pyodbc.connect('Driver=#;Server=#;Database=#') as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM table_name')
        columns_name = [column[0] for column in cursor.description]
        print(columns_name)

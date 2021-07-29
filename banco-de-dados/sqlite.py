import sqlite3 as db


connection = db.connectionnect('teste.db')

cursor = connection.cursor()

cursor.execute('PRAGMA Foreign_keys = ON;')
connection.commit()


cursor.execute('PRAGMA Foreign_keys;')
print(cursor.fetchone())

cursor.execute('PRAGMA Foreign_keys = OFF;')
connection.commit()

cursor.execute('PRAGMA Foreign_keys;')
print(cursor.fetchone())

# PRAGMA Foreign_key_list ( nome da tabela );

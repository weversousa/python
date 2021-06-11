from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker

from models import Estados

engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# Cada item é um Objeto, ao exibir um objeto ele virá codificado ou como você
# especificou no método __repr__.


# SQL:
# SELECT *
# FROM estados

estados = session.query(Estados)

for estado in estados:
    print(estado)

print("-" * 20)


# Para não exir o objeto em si, você pode exibir os seus atributos.
# A forma de acessar um atributo de um Objeto é usando a "Notação de Ponto".

# SQL:
# SELECT *
# FROM estados

session.query(Estados)

for estado in estados:
    print(estado.nome)

print("-" * 20)


# SQL:
# SELECT TOP 1 nome
# FROM estados
estado = session.query(Estados.nome).first()
print(estado)
print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE nome = 'São Pulo'

estados = session.query(Estados.nome).filter(Estados.nome == "São Paulo")

for estado in estados:
    print(estado)

print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE nome <> 'São Pulo'

estados = session.query(Estados.nome).filter(Estados.nome != "São Paulo")

for estado in estados:
    print(estado)

print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE nome = 'São Pulo' OR nome = 'Madrid'

estados = session.query(Estados.nome) \
                 .filter(or_(Estados.nome == "São Paulo",
                             Estados.nome == "Madrid"))

for estado in estados:
    print(estado)

print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE nome != 'São Pulo' AND nome != 'Madrid'

estados = session.query(Estados.nome) \
                 .filter(and_(Estados.nome != "São Paulo",
                              Estados.nome != "Madrid"))

for estado in estados:
    print(estado)

print("-" * 20)

estados = session.query(Estados.nome) \
                 .filter(Estados.nome != "São Paulo") \
                 .filter(Estados.nome != "Madrid")

for estado in estados:
    print(estado)

print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE nome LIKE 'B%'

estados = session.query(Estados.nome).filter(Estados.nome.like("B%"))

for estado in estados:
    print(estado)

print("-" * 20)


# SQL:
# SELECT nome
# FROM estados
# WHERE id IN(1, 2)

estados = session.query(Estados.nome).filter(Estados.id.in_((1, 2)))

for estado in estados:
    print(estado)

print("-" * 20)


# Pegar pelo ID
estado = session.query(Estados).get(2)
print(estado.nome)

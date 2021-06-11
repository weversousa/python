from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import asc, desc

from models import Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# SQL:
# SELECT id, nome
# FROM estados
# ORDER BY id ASC

print("----- id ASC -------")

estados = session.query(Estados.id, Estados.nome) \
                 .order_by(desc(Estados.id))

for estado in estados:
    print(estado.id, estado.nome)


# SQL:
# SELECT id, nome
# FROM estados
# ORDER BY nome DESC

print("----- nome DESC -------")

estados = session.query(Estados.id, Estados.nome) \
                 .order_by(asc(Estados.nome))

for estado in estados:
    print(estado.id, estado.nome)

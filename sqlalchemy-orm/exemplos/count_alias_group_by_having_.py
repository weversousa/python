from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Paises, Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# SQL:
# SELECT paises.nome, COUNT(*) AS "total"
# FROM paises INNER JOIN estados ON paises.id = estados.paises_id
# GROUP BY paises.nome

paises = session.query(Paises.nome, func.count("*").label("total")) \
                .filter(Paises.id == Estados.paises_id) \
                .group_by(Paises.nome)

for pais in paises:
    print(pais.nome, pais.total)

print("-" * 20)


# SQL:
# SELECT paises.nome, COUNT(*) AS "total"
# FROM paises INNER JOIN estados ON paises.id = estados.paises_id
# GROUP BY paises.nome
# HAVING total > 3

paises = session.query(Paises.nome, func.count("*").label("total")) \
                .filter(Paises.id == Estados.paises_id) \
                .group_by(Paises.nome) \
                .having(func.count("*") > 3)

for pais in paises:
    print(pais.nome, pais.total)

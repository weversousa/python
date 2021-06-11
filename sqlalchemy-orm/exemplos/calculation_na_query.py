from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import func

from models import Paises, Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# SQL:
# SELECT paises.nome, COUNT(*) AS "total", COUNT(*) - 1 AS "calculo"
# FROM paises INNER JOIN paises.id = estados.paises_id
# GROUP BY paises.nome

paises = session.query(Paises.nome, func.count("*").label("total"),
                       (func.count("*") - 1).label("calculo")) \
                .filter(Paises.id == Estados.paises_id) \
                .group_by(Paises.nome)


for pais in paises:
    print(pais.nome, pais.total, pais.calculo)

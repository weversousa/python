from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Paises, Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


""" O próprio SQLAlchemy faz a ligação INNER JOIN """

# SQL:
# SELECT paises.nome AS "pais",
#        estados.nome AS "estado"
# FROM paises INNER JOIN estados ON paises.id = estados.paises_id

print("----- INNER JOIN ------")

estado_com_pais = session.query((Paises.nome).label("pais"),
                                (Estados.nome).label("estado")) \
                         .filter(Paises.id == Estados.paises_id)

for ep in estado_com_pais:
    print(ep.pais, ep.estado)


# SQL:
# SELECT paises.nome AS "pais",
#        estados.nome AS "estado"
# FROM paises INNER JOIN estados ON paises.id = estados.paises_id
# WHERE paises.nome = 'Brasil'

print("----- INNER JOIN -- WHERE ------")

estado_com_pais = session.query((Paises.nome).label("pais"),
                                (Estados.nome).label("estado")) \
                         .filter(Paises.id == Estados.paises_id) \
                         .filter(Paises.nome == "Brasil")

for ep in estado_com_pais:
    print(ep.pais, ep.estado)


# SQL:
# SELECT paises.nome,
#        estados.nome
# FROM paises LEFT JOIN estados ON paises.id = estados.paises_id

print("----- paises LEFT JOIN estados ------")

estado_com_pais = session.query((Paises.nome).label("pais"),
                                (Estados.nome).label("estado")) \
                         .outerjoin(Estados, Paises.id == Estados.paises_id)

for ep in estado_com_pais:
    print(ep.pais, ep.estado)


# SQL:
# SELECT stados.nome,
#        paises.nome
# FROM estados LEFT JOIN paises ON estados.paises_id = paises.id

print("----- estados LEFT JOIN paises ------")

estado_com_pais = session.query((Estados.nome).label("estado"),
                                (Paises.nome).label("pais")) \
                         .outerjoin(Paises, Estados.paises_id == Paises.id)

for ep in estado_com_pais:
    print(ep.estado, ep.pais)

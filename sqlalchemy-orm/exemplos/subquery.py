from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Paises, Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# SELECT paises.nome, COUNT(*) AS "total"
# FROM paises JOIN estados ON paises.id == estados.paises_id
# GROUP BY paises.nome

# -------------------------
# \     nome      \ total \
# -------------------------
# \Brasil         \ 3     \
# \Espanha        \ 4     \
# \Estados Unidos \ 4     \
# -------------------------


# SQL:
# SELECT paises.nome AS "pais", COUNT(*) AS "total"
# FROM paises JOIN estados ON paises.id == estados.paises_id
# GROUP BY pais
# HAVING total >= (
#         SELECT COUNT(*)
#         FROM paises JOIN estados ON paises.id == estados.paises_id
#         WHERE paises.nome = 'Espanha'
#         )

# -------------------------
# \     nome      \ total \
# -------------------------
# \Espanha        \ 4     \
# \Estados Unidos \ 4     \
# -------------------------

minha_subquery = session.query((func.count(Paises.nome)).label("total")) \
                        .join(Estados, Paises.id == Estados.paises_id) \
                        .filter(Paises.nome == "Espanha") \
                        .subquery()


paises = session.query(Paises.nome.label("pais"),
                       func.count("*").label("total")) \
                .filter(Paises.id == Estados.paises_id) \
                .group_by(Paises.nome) \
                .having(func.count("*") >=
                        minha_subquery
                        ) \
                .all()

print(paises)


"""
A brincadeira é a seguinte:

Nas linhas 13 a 23 foi mostrado quantos Estados de cada país temos cadastrados.

Nas linhas 26 a 41 a gente filtrou os países que tem um total de Estados maior
ou igual ao números de Estados que tem o país da Espanha.


É importante enteder Subquery galerinha, e eu fiz um exemplo bem simples rsrsr.
"""

# Para usar um atributo de um Subquery a sintaxe é a seguinte:
# <nome subquery>.<c>.<nome atributo>

# Outra dica valiosa! Não foi fácil descobrir esse "c"...

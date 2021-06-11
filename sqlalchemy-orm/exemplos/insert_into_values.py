from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from models import Paises, Estados

engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()

# Para adicionar mais de uma valor, os valores são passados em uma lista.
session.add_all([
    Paises(nome="Estados Unidos"),
    Paises(nome="Brasil"),
    Paises(nome="Espanha"),
    Paises(nome="França"),
])

session.commit()

session.add_all([
    Estados(nome="São Paulo", paises_id=2),
    Estados(nome="Califórnia", paises_id=1),
    Estados(nome="Madrid", paises_id=3),
    Estados(nome="Bahia", paises_id=2),
    Estados(nome="New York", paises_id=1),
    Estados(nome="Barcelona", paises_id=3),
    Estados(nome="Rio de Janeiro", paises_id=2),
    Estados(nome="Washington", paises_id=1),
    Estados(nome="Alicante", paises_id=3),
    Estados(nome="Nova Jersey", paises_id=1),
])

session.commit()

# Um valor só não é em lista.
session.add(Estados(nome="Málaga", paises_id=3),)
session.add(Estados(nome="Roma", paises_id=5),)

session.commit()


# O reverso do commit... Você limpa a sessão e NÃO persiste os dados no banco.
session.flush()

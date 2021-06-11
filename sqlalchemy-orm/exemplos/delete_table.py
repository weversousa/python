from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Paises


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()


# SQL:
# DELETE
# FROM paises
# WHERE nome = 'França'

session.delete(session.query(Paises).filter(Paises.nome == "França")[0])
session.commit()

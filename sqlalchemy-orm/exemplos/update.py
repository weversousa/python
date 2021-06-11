from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Estados


engine = create_engine("sqlite:///weversousa.db")

Session = sessionmaker(bind=engine)
session = Session()

# Para atualizar um dado, você antes precisa pegar o objeto e depois alterar
# o atributo que deseja, e por fim dar um commit para consolidar a alteração.


# SQL:
# UPDATE estados
# SET nome = 'Amazonas'
# WHERE nome = 'Roma'

objeto_para_alterar = session.query(Estados).filter(Estados.nome == "Roma")[0]
objeto_para_alterar.nome = "Amazonas"

session.commit()

from supermercado.database import db
from supermercado.models import Produtos


def pegar_produtos_do_banco():
    return db.session.query(Produtos).all()

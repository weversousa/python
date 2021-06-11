from supermercado.database import db


class Produtos(db.Model):

    __tablename__ = 'produtos'

    id = db.Column(db.Integer, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='pk_produtos'),
        db.UniqueConstraint('nome', 'marca', name='uq_produtos_s'),
    )

    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

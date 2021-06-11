from supermercado.database import db
from supermercado.models import Produtos


def init_app(app):

    @app.cli.command()
    def criar_tabelas():
        """Cria todas as tabelas"""
        db.create_all()

    @app.cli.command()
    def popular_tabelas():
        """Vai popular todas as tabelas"""

        db.session.add_all([
            Produtos(nome='Arroz', marca='Albaruska', preco=28.30),
            Produtos(nome='Feijão', marca='Pantera', preco=9.70),
            Produtos(nome='Café', marca='Pelé', preco=11.30),
        ])

        db.session.commit()
        print('Produtos inseridos na tabela com sucesso.')

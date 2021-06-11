from brasileirao.database import db
from brasileirao.models import Estados, Times


def init_app(app):

    @app.cli.command()
    def criar_tabelas():
        """Cria todas as tabelas"""
        db.create_all()

    @app.cli.command()
    def popular_tabelas():
        """Vai popular todas as tabelas"""

        db.session.add_all([
            Estados(sigla="BA"),
            Estados(sigla="CE"),
            Estados(sigla="GO"),
            Estados(sigla="MG"),
            Estados(sigla="MT"),
            Estados(sigla="PE"),
            Estados(sigla="PR"),
            Estados(sigla="RJ"),
            Estados(sigla="RS"),
            Estados(sigla="SC"),
            Estados(sigla="SP"),
        ])

        db.session.commit()

        db.session.add_all([
            Times(nome="América", estado_id=4),
            Times(nome="Athletico", estado_id=7),
            Times(nome="Atlético", estado_id=3),
            Times(nome="Atlético", estado_id=4),
            Times(nome="Bahia", estado_id=1),
            Times(nome="Ceará", estado_id=2),
            Times(nome="Chapecoense", estado_id=10),
            Times(nome="Corinthians", estado_id=11),
            Times(nome="Cuibá", estado_id=5),
            Times(nome="Flamengo", estado_id=8),
            Times(nome="Fluminense", estado_id=8),
            Times(nome="Fortaleza", estado_id=2),
            Times(nome="Grêmio", estado_id=9),
            Times(nome="Internacional", estado_id=9),
            Times(nome="Juventude", estado_id=9),
            Times(nome="Palmeiras", estado_id=11),
            Times(nome="Bragantino", estado_id=11),
            Times(nome="Santos", estado_id=11),
            Times(nome="Sport Recife", estado_id=6),
            Times(nome="São Paulo", estado_id=11),
        ])

        db.session.commit()

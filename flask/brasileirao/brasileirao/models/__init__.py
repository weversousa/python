from brasileirao.database import db


class Estados(db.Model):

    __tablename__ = "estados"

    id = db.Column(db.Integer, autoincrement=True)
    sigla = db.Column(db.String(2), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint("id", name="pk_estados"),
        db.UniqueConstraint("sigla", name="uq_estados_sigla"),
    )

    def __init__(self, sigla):
        self.sigla = sigla


class Times(db.Model):

    __tablename__ = "times"

    id = db.Column(db.Integer, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False)
    estado_id = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint("id", name="pk_times"),
        db.ForeignKeyConstraint(
            ["estado_id"],
            ["estados.id"],
            name="fk_tmes_estado_id",
            ondelete='CASCADE'
        ),
        db.UniqueConstraint("nome", "estado_id", name="uq_times_nome_estado_id"),
    )

    estados = db.relationship("Estados", uselist=False)

    def __init__(self, nome, estado_id):
        self.nome = nome
        self.estado_id = estado_id

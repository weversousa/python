from sqlalchemy import (Column, Integer, String, PrimaryKeyConstraint,
                        UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base


# É a classe mãe que vai passar toda herança necessária para as classes filhas
# mapearem a tabela de um banco de dados.
Base = declarative_base()


class Paises(Base):
    __tablename__ = "paises"

    id = Column(Integer, autoincrement=True)
    nome = Column(String(20), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_paises"),
        UniqueConstraint("nome", name="uq_paises_nome"),
    )

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"<Paides(nome={self.nome})>"


class Estados(Base):
    __tablename__ = "estados"

    id = Column(Integer, autoincrement=True)
    nome = Column(String(20), nullable=False)
    paises_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_estados"),
        UniqueConstraint("nome", name="uq_estados_nome"),
    )

    def __init__(self, nome, paises_id):
        self.nome = nome
        self.paises_id = paises_id

    def __repr__(self):
        return f"<Estados(nome={self.nome})>"

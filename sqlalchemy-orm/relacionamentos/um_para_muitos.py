from sqlalchemy import create_engine, event, exc
from sqlalchemy.engine import Engine
from sqlalchemy import (Column, Integer, String, PrimaryKeyConstraint,
                        UniqueConstraint, ForeignKeyConstraint)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database/sqlalchemy_orm.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------------------------------------------------------

'''
Isso aqui é uma dica valiosa...
O SQLite por padrão desabilitada as funcionalidades de Chave Estrangeira.
Para saber mais pesquese sobre 'PRAGMAS SQLite'.
O procedimento abaixo serve para habilitar as funcinalidades.
(0,) ==> Significa: PRAGMA OFF.
(1,) ==> Significa: PRAGMA ON.
'''


@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')
    cursor.close()


pragma = engine.execute('PRAGMA Foreign_keys;').one()[0]
print('PRAGMA SQLite = ', pragma)

# -----------------------------------------------------------------------------


class Pai(Base):

    __tablename__ = 'pai'

    id = Column(Integer, autoincrement=True)
    nome = Column(String(30), nullable=False)
    sobrenome = Column(String(30), nullable=False)

    filhos = relationship('Filho', uselist=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_pai'),
        UniqueConstraint('nome', 'sobrenome', name='uq_pai_nome_sobrenome'),
    )

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __repr__(self):
        return f"<Pai(nome={self.nome}, sobrenome={self.sobrenome})>"


class Filho(Base):

    __tablename__ = 'filho'

    id = Column(Integer, autoincrement=True)
    nome = Column(String(30), nullable=False)
    sobrenome = Column(String(30), nullable=False)
    pai_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_filho'),
        UniqueConstraint('nome', 'sobrenome', name='uq_pai_nome_sobrenome'),
        ForeignKeyConstraint(['pai_id'], ['pai.id'], name='fk_filho_pai_id')
    )

    def __init__(self, nome, sobrenome, pai_id):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pai_id = pai_id

    def __repr__(self):
        return f"<Filho(nome={self.nome}, sobrenome={self.sobrenome})>"


# -----------------------------------------------------------------------------

''' Exclui e cria novamente as tabelas sempre que o código é executado '''

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# -----------------------------------------------------------------------------

filho_1 = Filho(nome='Filho1', sobrenome='Marques', pai_id=1)

try:
    session.add(filho_1)
    session.commit()
except exc.IntegrityError:
    session.rollback()
    print('Ocorreu um erro!')
    print('Isso não é possível, pois estamos usando chave estrangeira.')
    print('LEGAL! Pois o a função para ativar o PRAGMA do SQLite deu certo.')
    print('NÃO PODE ADICONAR UM FILHO QUE NÃO TENHA UM PAI CADASTRADO')
# -----------------------------------------------------------------------------

pai_1 = Pai(nome='João', sobrenome='Marques')
session.add(pai_1)
session.commit()
# -----------------------------------------------------------------------------

''' Tendo um Pai cadastrado, agora podemos cadastrar um Filho a ele '''
id_pai_1 = session.query(Pai.id).filter(Pai.sobrenome == 'Marques').one()[0]

filho_1 = Filho(nome='Marcos', sobrenome='Marques', pai_id=id_pai_1)
filho_2 = Filho(nome='Paula', sobrenome='Marques', pai_id=id_pai_1)
session.add_all([filho_1, filho_2])
session.commit()
# -----------------------------------------------------------------------------

''' Enfim a parte que nos interessa, a mágica do Relacionamento não precisamos
de uma query de ligação ou join para mostrar quem são os Filhos de cada Pai '''

for pai in session.query(Pai).all():
    print('NOME DO PAI: ', pai.nome)
    for filho in pai.filhos:
        print('NOME DO FILHO: ', filho.nome)

# Resultado:
# NOME DO PAI:  João
# NOME DO FILHO:  Marcos
# NOME DO FILHO:  Paula
# -----------------------------------------------------------------------------

''' Mais um Pai para ver que cada Pai estará associado somente ao seu Filho '''

pai_2 = Pai(nome='Maria', sobrenome='Pereira')
session.add(pai_2)
session.commit()

id_pai_2 = session.query(Pai.id).filter(Pai.sobrenome == 'Pereira').one()[0]

filho_3 = Filho(nome='Luciano', sobrenome='Pereira', pai_id=id_pai_2)
filho_4 = Filho(nome='Carlos', sobrenome='Pereira', pai_id=id_pai_2)
session.add_all([filho_3, filho_4])
session.commit()

print('----------------------------')
for pai in session.query(Pai).all():
    print('NOME DO PAI: ', pai.nome)
    for filho in pai.filhos:
        print('NOME DO FILHO: ', filho.nome)
    print()

# Resultado:
# ----------------------------
# NOME DO PAI:  João
# NOME DO FILHO:  Marcos
# NOME DO FILHO:  Paula

# NOME DO PAI:  Maria
# NOME DO FILHO:  Luciano
# NOME DO FILHO:  Carlos

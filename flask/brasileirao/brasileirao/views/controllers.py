from brasileirao.database import db
from brasileirao.models import Times


def pegar_times_do_banco():
    return db.session.query(Times).all()

from sqlalchemy import create_engine

from models import Base

engine = create_engine("sqlite:///weversousa.db")

Base.metadata.drop_all(engine)

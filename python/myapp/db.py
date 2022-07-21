from sqlalchemy import create_engine

from myapp import const
from myapp.model import Base

_engine = create_engine(const.DB_URL, future=True)


def get_engine():
    # not 100% sure it's safe to share around? Should be ok since it's conn
    #  pools right?
    return _engine


def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)


def drop_tables():
    engine = get_engine()
    Base.metadata.drop_all(engine)


def renew_tables():
    drop_tables()
    create_tables()

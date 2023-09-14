from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker, Session
from contextlib import contextmanager


class Base(MappedAsDataclass, DeclarativeBase):
    pass

SQLALCHEMY_DATABASE_URI: str = 'sqlite:///./quotes.db'
engine: Engine = create_engine(SQLALCHEMY_DATABASE_URI)
datbase_session: Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_all() -> None:
    Base.metadata.create_all(bind=engine)
    
def drop_all() -> None:
    Base.metadata.drop_all(bind=engine)

@contextmanager
def get_db() -> Session:
    try:
        db: Session = datbase_session()
        yield db
    finally:
        db.close()
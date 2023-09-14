from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base
from datetime import datetime


class Author(Base):
    __tablename__ = 'authors'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    birthday: Mapped[datetime]
    birthplace: Mapped[str]
    bio: Mapped[str]
    
    quotes = relationship('Quote', back_populates='author')
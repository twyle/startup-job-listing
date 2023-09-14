from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Tag(Base):
    
    __tablename__ = 'tags'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    quotes = relationship('Quote', secondary='quote_tag', lazy='dynamic', backref='tag')
    
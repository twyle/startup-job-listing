from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Quote(Base):
    __tablename__ = 'quotes'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    quote_content: Mapped[str]
    author_id: Mapped[str] = mapped_column(ForeignKey('authors.id'))
    tags = relationship('Tag', secondary='quote_tag', lazy='dynamic', backref='quote')
    author = relationship('Author', back_populates='quotes')
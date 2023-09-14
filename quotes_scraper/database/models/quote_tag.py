from ..database import Base
from sqlalchemy import Table, Column, String, ForeignKey


quote_tag = Table(
    'quote_tag',
    Base.metadata,
    Column('quote_id', String, ForeignKey('quotes.id')),
    Column('tag_id', String, ForeignKey('tags.id'))
)
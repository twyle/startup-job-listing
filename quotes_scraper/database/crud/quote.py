from ..models import Tag, Author, Quote
from ..database import get_db
from scrapy.item import Item
from uuid import uuid4


def create_quote(item: Item) -> None:
    quote: Quote = Quote(
        id=f'Quote_{str(uuid4())}',
        author_id=item['author_id'],
        quote_content=item['quote_content']
    )
    with get_db() as session:
        tags: list[Tag] = session.query(Tag).filter(Tag.id.in_(item['tag_ids'])).all()
        quote.tags = tags
        session.add(quote)
        session.commit()
        session.refresh(quote)
        return quote
from ..models import Author
from ..database import get_db
from scrapy.item import Item
from uuid import uuid4


def create_author(item: Item) -> None:
    author: Author = Author(
        name=item['author_name'],
        id=f'Author_{str(uuid4())}',
        birthday=item['author_birthday'],
        birthplace=item['author_bornlocation'],
        bio=item['author_bio']
    )
    with get_db() as session:
        session.add(author)
        session.commit()
        session.refresh(author)
        return author
    
def get_author(author_name: str) -> Author | None:
    with get_db() as session:
        author = session.query(Author).filter(Author.name == author_name).first()
        return author
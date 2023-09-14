from ..models import Tag
from ..database import get_db
from scrapy.item import Item
from uuid import uuid4


def create_tag(item: Item) -> None:
    tag: Tag = Tag(
        id=f'Tag_{str(uuid4())}',
        name=item['name']
    )
    with get_db() as session:
        session.add(tag)
        session.commit()
        session.refresh(tag)
        return tag
    
def get_tag(tag_name: str) -> Tag | None:
    with get_db() as session:
        tag: Tag = session.query(Tag).filter(Tag.name == tag_name).first()
        return tag
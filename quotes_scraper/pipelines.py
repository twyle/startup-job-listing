# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import create_all, get_db, drop_all
from .database.models import Author, Quote, quote_tag, Tag
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
from .database.crud import create_author, get_author, create_tag, get_tag, create_quote
from scrapy import Spider, Item
from .items import TagItem, QuoteItemSchema
from redis import Redis
from scrapy.exceptions import DropItem



class DropDuplicatesPipeline:
    def __init__(self) -> None:
        self.redis: Redis = Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    def process_item(self, item: Item, spider: Spider) -> Item:
        quote_content: str = item['quote_content']
        if self.redis.get(quote_content):
            raise DropItem(f'The quote alreasdy exists. {quote_content}')
        return item
    
class SaveQuotesPipeline:
    def __init__(self) -> None:
        self.redis: Redis = Redis(host='localhost', port=6379, db=0, decode_responses=True)
        create_all()
        
    def process_item(self, item: Item, spider: Spider) -> Item:
        page: str = item['page']
        author: Author | None = get_author(item['author_name'])
        if not author:
            author = create_author(item)
        self.redis.zincrby('quote_authors', 1, item['author_name'])
        quote_tag_ids: list[Tag] = []
        if 'tags' in item.fields:
            for tag_name in item['tags']:
                tag: Tag = get_tag(tag_name)
                if not tag:
                    tag = create_tag(TagItem(name=tag_name))
                quote_tag_ids.append(tag.id)
                self.redis.zincrby(f'quote_tags_{page}', 1, tag_name)
                self.redis.zincrby('quote_tags', 1, tag_name)
        quote_item: QuoteItemSchema = QuoteItemSchema(
            author_id=author.id,
            tag_ids=quote_tag_ids,
            quote_content=item['quote_content']
        )
        quote: Quote = create_quote(quote_item)
        quote_content: str = item['quote_content']
        self.redis.set(quote_content, quote_content)
        return item

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...extensions import redis
from ..database.schemas import PopularQuotesAuthor, PopularQuotesTag
from typing import Optional


home = APIRouter(
    prefix='/quotes',
    tags=['home']
)

@home.get('/popular_authors', status_code=200)
async def popular_authors():
    """Get the ten most popular quote authors."""
    authors: list[tuple[str, float]] = redis.zrevrange('quote_authors', 0, 10, withscores=True)
    authors: list[PopularQuotesAuthor] = [
        PopularQuotesAuthor(name=author[0], count=author[1]).model_dump()
        for author in authors
    ]
    return JSONResponse({"authors": authors})
    

@home.get('/popular_quotes', status_code=200)
async def popular_quotes(page: Optional[str] = None):
    """Get the ten most popular quote tags."""
    if page:
        tags: list[tuple[str, float]] = redis.zrevrange(f'quote_tags_{page}', 0, 10, withscores=True)
    else:
        tags: list[tuple[str, float]] = redis.zrevrange(f'quote_tags', 0, 10, withscores=True)
    tags: list[PopularQuotesTag] = [
        PopularQuotesTag(name=tag[0], count=tag[1]).model_dump()
        for tag in tags
    ]
    return JSONResponse({"tags": tags})
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from ...extensions import redis
from ..database.schemas import PopularQuotesAuthor, PopularQuotesTag
from typing import Optional
from elasticsearch import Elasticsearch
from .helpers import get_es_client, search_quotes, Quote


search = APIRouter(
    prefix='/quotes',
    tags=['search']
)

@search.get('/search_authors', status_code=200)
async def popular_authors():
    """Get the ten most popular quote authors."""
    return JSONResponse({"authors": 'authors'})
    

@search.get('/get_quotes', status_code=200)
async def get_quotes(
    query: str = Query(alias="q"),
    es_client: Elasticsearch = Depends(get_es_client),
) -> list[Quote]:
    if len(query.strip()) == 0:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid query",
        )
    quotes: list[Quote] = search_quotes(es_client, query)
    return quotes
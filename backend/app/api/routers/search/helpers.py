from elasticsearch import Elasticsearch
from ...config import es_auth, POSTS_INDEX_NAME
from ..database.schemas import Quote


def get_es_client():
    """Get the dependency for ES client."""
    es_client = Elasticsearch(
        es_auth.host,
        basic_auth=(es_auth.user, es_auth.password.get_secret_value()),
    )

    try:
        yield es_client
    finally:
        es_client.close()
        
        
def search_quotes(es_client: Elasticsearch, query: str):
    search_query = {
        "multi_match": {
            "query": query,
            "type": "most_fields",
            "operator": "and",
            "fields": [
                "quote_content^3",
                "quote_content.ngrams",
                "tags^2"
            ],
        }
    }

    results = es_client.search(
        index=POSTS_INDEX_NAME,
        query=search_query,
    )

    quotes_found: list[Quote] = [
        Quote(**hit["_source"]) for hit in results["hits"]["hits"]
    ]

    return quotes_found
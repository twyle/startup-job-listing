from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class ESAuth(BaseSettings):
    """Settings for Elasticsearch."""

    host: str = Field(env="ES_HOST", default="http://localhost:9200")
    user: str = Field(env="ES_USER", default="elastic")
    password: SecretStr = Field(env="ES_PASSWORD", default="elastic")


es_auth = ESAuth()

POSTS_INDEX_NAME = "quotes"

POSTS_INDEX_SETTINGS = {
    "analysis": {
        "analyzer": {
            "quotes_index_analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "autocomplete_filter",
                ],
            },
            "quotes_search_analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                ],
            },
        },
        "filter": {
            "autocomplete_filter": {
                "type": "edge_ngram",
                "min_gram": 1,
                "max_gram": 20,
            },
        },
    },
}


POSTS_INDEX_MAPPINGS = {
    "properties": {
        "tags": {"type": "text"},
        "quote_content": {
            "type": "text",
            "search_analyzer": "quotes_search_analyzer",
            "fields": {
                "ngrams": {
                    "type": "text",
                    "analyzer": "quotes_index_analyzer",
                    "search_analyzer": "quotes_search_analyzer",
                },
            },
        },
    }
}

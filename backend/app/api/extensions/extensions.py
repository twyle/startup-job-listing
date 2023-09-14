from redis import Redis
from elasticsearch import Elasticsearch
from ..config import es_auth

redis: Redis = Redis(host='localhost', port=6379, db=0, decode_responses=True)

es_client = Elasticsearch(
    es_auth.host,
    basic_auth=(es_auth.user, es_auth.password.get_secret_value()),
)
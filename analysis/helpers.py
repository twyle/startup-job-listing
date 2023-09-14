from celery import Celery
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from redis import Redis
from json import dumps

load_dotenv()


class BaseConfig(BaseSettings):
    celery_broker_url: str
    celery_result_backend: str
    redis_host: str
    
config = BaseConfig()

celery = Celery(__name__)
celery.conf.broker_url = config.celery_broker_url
celery.conf.result_backend = config.celery_result_backend
redis: Redis = Redis(host=config.redis_host, port=6379, db=0, decode_responses=True)

@celery.task(name="analyze_quote")
def analyze_quote(quote: dict) -> dict:
    analyzed_quote: dict = quote
    analyzed_quote.update({'result': 'Some result'})
    redis.publish('analyzed_quotes', dumps(analyzed_quote))
    return analyzed_quote

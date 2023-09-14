from helpers import analyze_quote, redis
from json import loads


def quotes():
    sub = redis.pubsub()
    sub.subscribe('quotes')
    for message in sub.listen():
        if message and isinstance(message['data'], str):
            quote: dict = message['data']
            task = analyze_quote.delay(loads(quote))
            print({'Task Id': task.id})
            
if __name__ == '__main__':
    while True:
        quotes()
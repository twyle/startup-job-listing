from helpers import redis


def analyzed_quotes():
    sub = redis.pubsub()
    sub.subscribe('analyzed_quotes')
    for message in sub.listen():
        if message and isinstance(message['data'], str):
            quote: dict = message['data']
            print(quote)
            
if __name__ == '__main__':
    while True:
        analyzed_quotes()
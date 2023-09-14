from redis import Redis

redis = Redis()

page = '1'
res = redis.zrevrange(f'quote_authors', 0, 10, withscores=True)
print(res)
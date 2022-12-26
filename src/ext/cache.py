from time import sleep
from redis import StrictRedis


def redis_connect(decode_responses):
    redis_port = 6379
    redis_host = 'localhost'
    loop = True
    while loop:
        try:
            redis = StrictRedis(host=redis_host, port=redis_port, decode_responses=decode_responses)
            loop = False
            return redis
        except ConnectionError as e:
            print(f'{e}; Something Wrong')
            sleep(2)


def cache_expire(time=None):
    def decorator(f):
        def closure(*args, **kwargs):
            response = f(*args, **kwargs)
            function_name = f.__name__
            redis = redis_connect(decode_responses=False)
            cached = redis.get(function_name)
            if cached:
                return cached
            else:
                redis.setex(function_name, time, response)
                return response
        return closure
    return decorator


def cache(f):
    def closure(*args, **kwargs):
        response = f(*args, **kwargs)
        function_name = f.__name__
        redis = redis_connect(decode_responses=False)
        cached = redis.get(function_name)
        if cached:
            return cached
        else:
            redis.set(function_name, response)
            return response
    return closure


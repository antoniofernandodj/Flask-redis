from .ext.cache import redis_connect
import requests
from flask import make_response
from pprint import pprint
import inspect
from werkzeug.datastructures import Headers


def get_content(url, content_type):
    key = inspect.stack()[1][3]
    cached = redis_connect(decode_responses=False).get(key)
    print(f'key {key}')
    if cached:
        print('cached')
        content = cached
    else:
        print('not cached')
        content = requests.get(url).content
        redis_connect(decode_responses=False).set(key, content)
    response = make_response(content)
    response.headers = Headers([
        ('Content-Type', 'content_type')
    ])
    return response

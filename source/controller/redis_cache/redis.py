import redis
from fastapi import Request, Response
from typing import Optional

redis_client = redis.Redis(host='localhost', port=6379)

def cache_response(ttl: Optional[int] = None):
    def decorator(func):
        async def wrapper(request: Request) -> Response:
            response = await func(request)
            if ttl is not None:
                response.headers['Cache-Control'] = f'max-age={ttl}'
                redis_client.set(f'cache:{request.url.path}', response.body, ex=ttl)
            return response
        return wrapper
    return decorator
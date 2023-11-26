import json
import redis
import configuration


connection = redis.Redis(
    host=f"{configuration.REDIS_HOST}",
    port=f"{configuration.REDIS_PORT}",
    decode_responses=True
)


def set_init():
    connection.set('init', "OK")


def get_init() -> bool:
    return connection.get('init') == "OK"


def add_object(key: str, obj: dict):
    connection.set(key, json.dumps(obj))


def remove_object(key: str):
    connection.delete(key)


def get_object(key: str):
    obj = connection.get(key)
    if obj:
        return json.loads(obj)
    return None

import redis
import configuration


connection = redis.Redis(
    host=f"{configuration.REDIS_HOST}",
    port=f"{configuration.REDIS_PORT}",
    decode_responses=True,
    prefix="user"
)


def set_init():
    connection.set('init', True)


def get_init() -> bool:
    return connection.get('init')


def add_object(key: str, obj: dict):
    pass


def get_object(key):
    pass

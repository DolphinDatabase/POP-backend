import os


OAUTH_SECRET_KEY = os.getenv("OAUTH_SECRET_KEY", "SECRET")
OAUTH_ALGORITHM = os.getenv("OAUTH_ALGORITHM", "HS256")
OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("OAUTH_TOKEN_EXPIRE", "30"))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://pop:pop@localhost:5432/pop")
# DATABASE_URL = os.getenv("DATABASE_URL",
#                          "postgresql://postgres:admin@localhost:5432/postgres")

LOCAL_CASSANDRA_URL = os.environ.get("CASSANDRA_URL", "localhost")

EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

REDIS_HOST = os.environ.get("REDIS_URL", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
import os


OAUTH_SECRET_KEY = os.getenv("OAUTH_SECRET_KEY", "SECRET")
OAUTH_ALGORITHM = os.getenv("OAUTH_ALGORITHM", "HS256")
OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("OAUTH_TOKEN_EXPIRE", "30"))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@localhost:5432/postgres")
# DATABASE_URL = os.getenv("DATABASE_URL",
#                          "postgresql://postgres:admin@localhost:5432/postgres")
LOCAL_REDIS_URL = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379")
LOCAL_CASSANDRA_URL = os.environ.get("CASSANDRA_URL", "localhost")

EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

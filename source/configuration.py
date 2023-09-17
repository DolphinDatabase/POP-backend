import os


OAUTH_SECRET_KEY = os.getenv("OAUTH_SECRET_KEY", "SECRET")
OAUTH_ALGORITHM = os.getenv("OAUTH_ALGORITHM", "HS256")
OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("OAUTH_TOKEN_EXPIRE", "30"))

DATABASE_URL = os.getenv("DATABASE_URL",
                         "postgresql://postgres:root@localhost:5432/pop")

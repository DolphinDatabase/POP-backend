from jose import JWTError, jwt
from datetime import datetime, timedelta
import configuration


def authenticate_user(username: str, password: str):
    return {
        'username': 'bea',
    }


def create_access_token(data: dict):
    access_token_expires = timedelta(minutes=configuration.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, configuration.SECRET_KEY, algorithm=configuration.ALGORITHM)
    return encoded_jwt

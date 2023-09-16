from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy import select

import configuration
import database
import crypt
from model import Usuario


def authenticate_user(email: str, password: str) -> Usuario:
    usuario: Usuario

    with database.SessionLocal() as session:
        statement = select(Usuario).filter_by(email=email)
        usuario = session.execute(statement).first()

    if not usuario or crypt.hash_password(password) != usuario.password:
        return False

    return usuario


def create_access_token(data: dict):
    access_token_expires = timedelta(
            minutes=configuration.OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             configuration.OATUH_SECRET_KEY,
                             algorithm=configuration.OAUTH_ALGORITHM)
    return encoded_jwt

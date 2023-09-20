from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy import select
import configuration
import database
import crypt
from model import Usuario
from .usuario_service import UsuarioService


def authenticate_user(email: str, password: str) -> Usuario:
    usuario: Usuario = UsuarioService.get_usuario_by_email(email)
    print(crypt.hash_password(password))
    print(usuario.senha)
    if not usuario or crypt.hash_password(password) != usuario.senha:
        return False

    return usuario


def create_access_token(data: dict) -> (str, float):
    to_encode = data.copy()
    access_token_expires = timedelta(minutes=configuration.OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = (datetime.utcnow() + access_token_expires).timestamp()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             configuration.OAUTH_SECRET_KEY,
                             algorithm=configuration.OAUTH_ALGORITHM)
    return encoded_jwt, expire


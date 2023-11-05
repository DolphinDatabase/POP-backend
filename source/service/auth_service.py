from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
import configuration
import crypt
from controller.exceptions import (
    credentials_exception,
    role_exception,
    requires_accept_exception,
)
from model import Usuario, Grupo
from schema import Token, TokenData

from .termo_service import TermoService
from .usuario_service import UsuarioService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


def get_authenticated_user(token: Annotated[str, Depends(oauth2_scheme)]) -> Usuario:
    try:
        payload = jwt.decode(
            token,
            configuration.OAUTH_SECRET_KEY,
            algorithms=[configuration.OAUTH_ALGORITHM],
        )

        token_data: TokenData = TokenData.model_validate(payload)

        if token_data.user is None or token_data.expire < datetime.utcnow().timestamp():
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = UsuarioService.get_usuario_by_email(token_data.user)

    if user is None:
        raise credentials_exception

    return user


def get_active_user(user: Annotated[Usuario, Depends(get_authenticated_user)]):
    if ((not user.ativo or not TermoService.get_last_termo_aceite(user).aceite)
            and user.grupo != Grupo.ADMINISTRADOR.value):
        raise requires_accept_exception

    return user


def get_adm_user(user: Annotated[Usuario, Depends(get_active_user)]):
    if user.grupo != Grupo.ADMINISTRADOR.value:
        raise role_exception

    return user


def authenticate_user(email: str, password: str) -> Token:
    usuario: Usuario = UsuarioService.get_usuario_by_email(email)

    if not usuario or crypt.hash_password(password) != usuario.senha:
        raise credentials_exception

    return create_access_token(usuario)


def create_access_token(usuario: Usuario) -> Token:
    interval_until_expires = timedelta(
        minutes=configuration.OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    expire = (datetime.utcnow() + interval_until_expires).timestamp()
    token_data = TokenData(user=usuario.email, expire=expire)

    jwt_token = jwt.encode(
        token_data.model_dump(),
        configuration.OAUTH_SECRET_KEY,
        algorithm=configuration.OAUTH_ALGORITHM,
    )
    return Token(access_token=jwt_token, expire=expire, token_type="bearer", role=usuario.grupo)

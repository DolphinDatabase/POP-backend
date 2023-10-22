from typing import Annotated
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from model import Token, Usuario
from schema.usuario_schema import GetUsuario
import service
import configuration
from .redis_cache.redis import cache_response


router = APIRouter(
    prefix='/auth',
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )

role_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Role unauthorized",
    headers={"WWW-Authenticate": "Bearer"},
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, configuration.OAUTH_SECRET_KEY, algorithms=[configuration.OAUTH_ALGORITHM])

        email: str = payload.get("sub")
        expire_time: int = payload.get("exp")

        if email is None or expire_time < datetime.utcnow().timestamp():
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = service.UsuarioService.get_usuario_by_email(email)

    if user is None:
        raise credentials_exception
    return user


def get_adm_user(user: Annotated[Usuario, Depends(get_current_user)]):
    print(user.adm)
    if user.adm:
        return user
    else:
        raise role_exception


@router.post("/", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = service.authenticate_user(
            form_data.username,
            form_data.password
            )
    if not user:
        raise credentials_exception
    
    access_token, expire = service.create_access_token(
        data={"sub": user.email}
    )

    return {"access_token": access_token, "expire": expire, "token_type": "bearer"}


@router.get("/", response_model=GetUsuario)
@cache_response(ttl=3600)
async def get_current(user: Annotated[Usuario, Depends(get_current_user)]):
    return user


@router.put("/", response_model=Token)
async def refresh_access_token(
    user: Annotated[Usuario, Depends(get_current_user)]
):
    access_token, expire, role = service.create_access_token(
        data={"sub": user.email}
    )
    role = "adm" if user.adm else "user"
    return {"access_token": access_token, "expire": expire, "role": role, "token_type": "bearer"}

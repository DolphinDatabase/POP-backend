from typing import Annotated
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_redis_cache import cache_one_hour

from model import Usuario
from schema import Token, GetUsuario
from service import auth_service

router = APIRouter(
    prefix="/auth",
)


@router.post("/", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return auth_service.authenticate_user(form_data.username, form_data.password)


@router.get("/", response_model=GetUsuario)
@cache_one_hour()
async def get_current(user: Annotated[Usuario, Depends(auth_service.get_active_user)]):
    return user


@router.put("/", response_model=Token)
async def refresh_access_token(
    user: Annotated[Usuario, Depends(auth_service.get_active_user)]
):
    return auth_service.create_access_token(user)

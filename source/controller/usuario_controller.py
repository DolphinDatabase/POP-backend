from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from model import Usuario
from service import UsuarioService, auth_service
from schema import GetUsuario, CreateUsuario, BaseUsuario, Token
from fastapi_redis_cache import cache_one_hour

router = APIRouter(prefix="/usuario")


@router.post("/", response_model=Token)
async def create(usuario: CreateUsuario):
    UsuarioService.create_usuario(usuario)
    return auth_service.authenticate_user(usuario.email, usuario.senha)


@router.get("/", response_model=GetUsuario)
@cache_one_hour()
async def get(user: Annotated[Usuario, Depends(auth_service.get_active_user)]):
    return GetUsuario(
        id=user.id, nome=user.nome, doc=user.doc, email=user.email, grupo=user.grupo
    )


@router.put("/", response_model=GetUsuario)
async def update(
    usuario: BaseUsuario,
    user: Annotated[Usuario, Depends(auth_service.get_active_user)],
):
    return UsuarioService.update_usuario(usuario)


@router.delete("/", response_model=GetUsuario)
async def delete(user: Annotated[Usuario, Depends(auth_service.get_active_user)]):
    return UsuarioService.delete_usuario(user)

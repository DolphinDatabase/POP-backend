from typing import Annotated

from fastapi import APIRouter, Depends

from model import Usuario
from service import UsuarioService, auth_service
from schema import GetUsuario, CreateUsuario, UpdateUsuario, Token
from fastapi_redis_cache import cache_one_hour

router = APIRouter(prefix="/usuario")

usuario_service = UsuarioService()
usuario_service.init_cache()


@router.post("/", response_model=Token)
async def create(usuario: CreateUsuario):
    usuario_service.create_usuario(usuario)
    return auth_service.authenticate_user(usuario.email, usuario.senha)


@router.get("/", response_model=GetUsuario)
@cache_one_hour()
async def get(user: Annotated[Usuario, Depends(auth_service.get_active_user)]):
    return GetUsuario(
        id=user.id, nome=user.nome, doc=user.doc, email=user.email, grupo=user.grupo
    )


@router.put("/", response_model=GetUsuario)
async def update(
    usuario: UpdateUsuario,
    user: Annotated[Usuario, Depends(auth_service.get_active_user)],
):
    return usuario_service.update_usuario(usuario, user)


@router.delete("/", response_model=None)
async def delete(user: Annotated[Usuario, Depends(auth_service.get_active_user)]):
    return f"Deleted user {usuario_service.deactivate_user(user)}"

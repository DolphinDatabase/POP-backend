from fastapi import APIRouter, HTTPException
from service import UsuarioService
from schema import GetUsuario, CreateUsuario, UsuarioBase, CreateHistorico
from .redis_cache.redis import cache_response

router = APIRouter(
    prefix='/usuario'
)


@router.post('/', response_model=GetUsuario)
async def create(usuario: CreateUsuario):
    u = UsuarioService.create_usuario(usuario)
    return u


@router.get('/{id}', response_model=GetUsuario)
@cache_response(ttl=3600)
async def get(id: int):
    try:
        return UsuarioService.get_usuario(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.put('/sign/{id}', response_model=GetUsuario)
async def sign(id: int):
    try:
        return UsuarioService.usuario_sign(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.put('/{id}', response_model=GetUsuario)
async def update(id: int, usuario: UsuarioBase):
    try:
        return UsuarioService.update_usuario(id, usuario)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.delete('/{id}')
async def delete(id: int):
    try:
        UsuarioService.delete_usuario(id)
    except Exception as e:
         raise HTTPException(status_code=e.args[0], detail=e.args[1])

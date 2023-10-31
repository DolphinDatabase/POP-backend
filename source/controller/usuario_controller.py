from fastapi import APIRouter, HTTPException
from service import UsuarioService
from schema import GetUsuario, CreateUsuario, UsuarioBase

router = APIRouter(
    prefix='/usuario'
)


@router.get('/', response_model=GetUsuario)
async def get(id: int):
    try:
        return UsuarioService.get_usuario(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.post('/', response_model=GetUsuario)
async def create(usuario: CreateUsuario):
    return UsuarioService.create_usuario(usuario)


@router.put('/', response_model=GetUsuario)
async def update(usuario: UsuarioBase):
    try:
        return UsuarioService.update_usuario(id, usuario)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.delete('/')
async def delete():
    try:
        UsuarioService.delete_usuario(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])

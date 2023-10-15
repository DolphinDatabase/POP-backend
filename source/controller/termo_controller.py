from fastapi import APIRouter, HTTPException, Depends
from service import TermoService
from schema import TermoBase, GetTermo
from model import Usuario
from typing import Annotated
from .auth_controller import get_adm_user

router = APIRouter(
    prefix='/termo'
)


@router.post('/', response_model=GetTermo)
async def create(termo: TermoBase, user: Annotated[Usuario, Depends(get_adm_user)]):
    return TermoService.create_termo(termo)


@router.get('/', response_model=list[GetTermo])
async def index():
    return TermoService.index_termo()


@router.get('/last')
async def last(proprietario: bool = False):
    try:
        return TermoService.get_last(proprietario)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.get('/{id}', response_model=GetTermo)
async def get(id: int):
    try:
        return TermoService.get_termo(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])


@router.put('/{id}', response_model=GetTermo)
async def update(id: int, termo: TermoBase, user: Annotated[Usuario, Depends(get_adm_user)]):
    try:
        return TermoService.update_termo(id, termo)
    except:
        raise HTTPException(404)


@router.delete('/{id}')
async def delete(id: int, user: Annotated[Usuario, Depends(get_adm_user)]):
    try:
        TermoService.delete_termo(id)
    except:
        raise HTTPException(404)

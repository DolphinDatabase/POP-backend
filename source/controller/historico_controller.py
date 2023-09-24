from fastapi import APIRouter, Depends
from schema import CreateHistorico,GetHistorico
from service import HistoricoService
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user

router = APIRouter(
    prefix='/historico'
)

@router.get('/{id}',response_model=list[GetHistorico])
async def get_by_usuario(id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    return HistoricoService.get_historico_by_user(id) 
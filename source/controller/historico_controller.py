from fastapi import APIRouter, Depends
from schema import CreateHistorico,GetHistorico
from service import HistoricoService
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user
from fastapi_redis_cache import cache_one_hour

router = APIRouter(
    prefix='/historico',
    dependencies=[Depends(get_current_user)]
)


@router.get('/{id}', response_model=list[GetHistorico])
@cache_one_hour()
async def get_by_usuario(id: int):
    return HistoricoService.get_historico_by_user(id)

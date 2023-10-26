
from fastapi import Depends,APIRouter, HTTPException
from service import operacao_service
from schema import schemas
from database import engine, Base
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user
from fastapi_redis_cache import cache_one_hour

router = APIRouter(
    prefix="/operacao",
    dependencies=[Depends(get_current_user)]
)


@router.get('/', response_model=list[schemas.Operacao])
@cache_one_hour()
async def get_operacoes():
    return operacao_service.get_operacaos()


@router.get('/{id}', response_model=schemas.Operacao)
@cache_one_hour()
async def get(id: int):
    try:
        return operacao_service.get_operacao(id)
    except:
        raise HTTPException(404)

from fastapi import Depends, APIRouter, HTTPException
from service import operacao_service
from schema import schemas
from .auth_controller import auth_service
from fastapi_redis_cache import cache_one_hour

router = APIRouter(
    prefix="/operacao", dependencies=[Depends(auth_service.get_active_user)]
)


@router.get("/", response_model=list[schemas.Operacao])
@cache_one_hour()
async def get_operacoes():
    return operacao_service.get_operacaos()


@router.get("/{operacao_id}", response_model=schemas.Operacao)
@cache_one_hour()
async def get(operacao_id: int):
    try:
        return operacao_service.get_operacao(operacao_id)
    except Exception:
        raise HTTPException(404)

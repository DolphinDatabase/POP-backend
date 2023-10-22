
from fastapi import Depends, APIRouter, HTTPException
from service import operacao_service
from schema import schemas
from .auth_controller import get_current_user

router = APIRouter(
    prefix="/operacao",
    dependencies=[Depends(get_current_user)]
)


@router.get('/', response_model=list[schemas.Operacao])
async def get_operacoes():
    return operacao_service.get_operacaos()


@router.get('/{id}', response_model=schemas.Operacao)
async def get(id: int):
    try:
        return operacao_service.get_operacao(id)
    except Exception:
        raise HTTPException(404)

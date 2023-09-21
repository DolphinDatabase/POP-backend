
from fastapi import APIRouter, HTTPException

from service import operacao_service
from schema import schemas
from database import engine, Base

# Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/operacao")


@router.get('/', response_model=list[schemas.Operacao])
async def get_operacaos():
    return operacao_service.get_operacaos()


@router.get('/{id}', response_model=schemas.Operacao)
async def get(id:int):
    try:
        return operacao_service.get_operacao(id)
    except:
        raise HTTPException(404)

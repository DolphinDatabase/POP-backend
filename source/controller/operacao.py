
from fastapi import Depends,APIRouter, HTTPException
from service import operacao_service
from schema import schemas
from database import engine, Base
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user

router = APIRouter(prefix="/operacao")

@router.get('/', response_model=list[schemas.Operacao])
async def get_operacaos(user: Annotated[Usuario, Depends(get_current_user)]):
    return operacao_service.get_operacaos()


@router.get('/{id}', response_model=schemas.Operacao)
async def get(id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    try:
        return operacao_service.get_operacao(id)
    except:
        raise HTTPException(404)

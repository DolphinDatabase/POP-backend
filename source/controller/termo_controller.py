from fastapi import APIRouter, HTTPException, Depends
from pydantic import ValidationError
from threading import Thread
from service import TermoService, EmailService
from schema import BaseTermo, GetTermo, AcceptTermo
from model import Usuario, Grupo
from typing import Annotated
from .auth_controller import auth_service
from .exceptions import validation_error
from fastapi_redis_cache import cache_one_hour

router = APIRouter(prefix="/termo")


@router.get("/")
async def get(user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)]):
    if user.grupo == Grupo.ADMINISTRADOR.value:
        termos = TermoService.list_termo()
        return {"termos": termos}
    return TermoService.get_last_termo_aceite(user)


@router.post("/", response_model=GetTermo)
async def post(
    termo: BaseTermo,
    user: Annotated[Usuario, Depends(auth_service.get_adm_user)],
):
    termo_criado = TermoService.create_termo(termo)
    EmailService().notify_group(termo.grupo)
    return termo_criado


@router.put("/", response_model=AcceptTermo)
async def put(
        termo: AcceptTermo,
        user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)],
):
    return TermoService.accept_termo(user, termo)

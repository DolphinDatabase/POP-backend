from fastapi import APIRouter, HTTPException, Depends
from pydantic import ValidationError
from threading import Thread
from service import TermoService, EmailService
from schema import BaseTermo, GetTermo, AcceptTermo
from schema.termo_schema import AcceptCondicao
from model import Usuario, Grupo
from typing import Annotated
from .auth_controller import auth_service
from .exceptions import validation_error
from fastapi_redis_cache import cache_one_hour

router = APIRouter(prefix="/termo")


def clean_termo(termo):
    del termo.aceites
    for condicao in termo.condicoes:
        del condicao.aceites
    return termo


@router.get("/", response_model=None)
async def get(user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)]):
    if user.grupo == Grupo.ADMINISTRADOR.value:
        termos = TermoService.list_termo()
        termos = [clean_termo(termo) for termo in termos]
        return {"termos": termos}

    termo = TermoService.get_last_termo_aceite(user)
    return clean_termo(termo)


@router.post("/", response_model=GetTermo)
async def post(
    termo: BaseTermo,
    user: Annotated[Usuario, Depends(auth_service.get_adm_user)],
):
    EmailService().notify_group(termo.grupo)
    termo_criado = TermoService.create_termo(termo)
    return termo_criado


@router.put("/", response_model=AcceptTermo)
async def put(
        termo: AcceptTermo,
        user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)],
):
    return TermoService.accept_termo(user, termo)

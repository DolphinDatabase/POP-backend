from fastapi import APIRouter, HTTPException, Depends
from pydantic import ValidationError

from service import TermoService
from schema import BaseTermo, GetTermo, AcceptTermo
from model import Usuario, Grupo
from typing import Annotated
from .auth_controller import auth_service
from .exceptions import validation_error
from fastapi_redis_cache import cache_one_hour

router = APIRouter(
    prefix='/termo'
)


@router.get('/')
@cache_one_hour()
async def get(user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)]):
    if user.grupo == Grupo.ADMINISTRADOR.value:
        termos = TermoService.list_termo()
        return {"termos": termos}
    return TermoService.get_last_termo_aceite(user)


@router.post('/')
@cache_one_hour()
async def post(termo: BaseTermo | AcceptTermo, user: Annotated[Usuario, Depends(auth_service.get_authenticated_user)]):
    try:
        if user.grupo == Grupo.ADMINISTRADOR.value:
            termo = BaseTermo.model_validate(termo)
            return TermoService.create_termo(termo)

        termo = AcceptTermo.model_validate(termo)
        return TermoService.accept_termo(user, termo)
    except ValidationError:
        raise validation_error

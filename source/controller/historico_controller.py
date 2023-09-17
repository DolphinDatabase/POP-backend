from fastapi import APIRouter, HTTPException
from schema import CreateHistorico,GetHistorico
from service import HistoricoService

router = APIRouter(
    prefix='/historico'
)

@router.get('/{id}',response_model=list[GetHistorico])
async def get_by_usuario(id:int):
    return HistoricoService.get_historico_by_user(id) 
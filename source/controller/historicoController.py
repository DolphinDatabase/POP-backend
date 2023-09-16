from fastapi import APIRouter, HTTPException
import service.historicoService as hService
import schema.historicoSchema as hSchema

router = APIRouter(
    prefix='/historico',
    responses={404: {"description": "historico not found"}}
)

@router.post('/',response_model=hSchema.HistoricoBase)
def create(historico:hSchema.HistoricoBase):
    return hService.create_historico(historico)
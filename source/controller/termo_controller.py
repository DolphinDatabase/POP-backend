from fastapi import APIRouter, HTTPException
from service import TermoService
from schema import TermoBase,GetTermo

router = APIRouter(
    prefix='/termo'
)


@router.post('/',response_model=GetTermo)
async def create(termo: TermoBase):
    return TermoService.create_termo(termo)


@router.get('/', response_model=list[GetTermo])
async def index():
    return TermoService.index_termo()

@router.get('/last')
async def last(proprietario:bool = False):
    try:
        return TermoService.get_last(proprietario)
    except Exception as e:
        raise HTTPException(status_code=e.args[0],detail=e.args[1])

@router.get('/{id}', response_model=GetTermo)
async def get(id:int):
    try:
        return TermoService.get_termo(id)
    except Exception as e:
        raise HTTPException(status_code=e.args[0],detail=e.args[1])

@router.put('/{id}',response_model=GetTermo)
async def update(id:int, termo: TermoBase):
    try:
        return TermoService.update_termo(id,termo)
    except:
        raise HTTPException(404)

@router.delete('/{id}')
async def delete(id:int):
    try:
        TermoService.delete_termo(id)
    except:
        raise HTTPException(404)

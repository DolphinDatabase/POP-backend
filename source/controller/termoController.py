from fastapi import APIRouter, HTTPException
from service.termoService import create_termo,index_termo,get_termo,update_termo,delete_termo,get_last
from schema.termoSchema import TermoBase,Termo

router = APIRouter(
    prefix='/termo',
    responses={404: {"description": "termo not found"}}
)

@router.post('/',response_model=Termo)
async def create(termo: TermoBase):
    return create_termo(termo)

@router.get('/', response_model=list[Termo])
async def index():
    return index_termo()

@router.get('/{id}', response_model=Termo)
async def get(id:int):
    try:
        return get_termo(id)
    except:
        raise HTTPException(404)

@router.get('/last', response_model=Termo)
async def get(id:int):
    try:
        return get_last()
    except:
        raise HTTPException(404)

@router.put('/{id}',response_model=Termo)
async def update(id:int, termo: TermoBase):
    try:
        return update_termo(id,termo)
    except:
        raise HTTPException(404)

@router.delete('/{id}')
async def delete(id:int):
    try:
        delete_termo(id)
    except:
        raise HTTPException(404)
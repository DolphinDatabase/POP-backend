from fastapi import Depends, HTTPException, APIRouter
from service import gleba_service
from schema import schemas
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user
from fastapi_redis_cache import cache_one_hour

router = APIRouter(prefix="/gleba")

@router.get('/estado/{estado}', response_model=schemas.FeatureCollections)
@cache_one_hour()
async def get_by_estado(estado:str,user: Annotated[Usuario, Depends(get_current_user)],skip: int = 0, limit: int = 100):
    return gleba_service.get_gleba_by_estado(estado,skip,limit)

@router.get('/location', response_model=schemas.FeatureCollections)
@cache_one_hour()
async def get_by_estado(user: Annotated[Usuario, Depends(get_current_user)],lat:float,long:float,size:float,skip: int = 0, limit: int = 100):
    return gleba_service.get_gleba_by_location(lat,long,size,skip,limit)

@router.get('/', response_model=schemas.FeatureCollections)
@cache_one_hour()
async def get_glebas(user: Annotated[Usuario, Depends(get_current_user)],skip: int = 0, limit: int = 100):
    return gleba_service.get_glebas(skip,limit)

@router.get('/{id}', response_model=schemas.Feature)
@cache_one_hour()
async def get(id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    try:
        return gleba_service.get_gleba(id)
    except:
        raise HTTPException(404)

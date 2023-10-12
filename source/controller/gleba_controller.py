from fastapi import Depends, HTTPException, APIRouter
from service import gleba_service
from schema import schemas
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user

router = APIRouter(
    prefix="/gleba",
    dependencies=[Depends(get_current_user)]
)


@router.get('/estado/{estado}', response_model=schemas.FeatureCollections)
async def get_by_estado(estado: str, skip: int = 0, limit: int = 100):
    return gleba_service.get_gleba_by_estado(estado, skip, limit)


@router.get('/location', response_model=schemas.FeatureCollections)
async def get_by_estado(lat: float, long: float):
    return gleba_service.get_gleba_by_location(lat, long)


@router.get('/', response_model=schemas.FeatureCollections)
async def get_glebas(skip: int = 0, limit: int = 100):
    return gleba_service.get_glebas(skip, limit)


@router.get('/{id}', response_model=schemas.Feature)
async def get(id: int):
    try:
        return gleba_service.get_gleba(id)
    except:
        raise HTTPException(404)

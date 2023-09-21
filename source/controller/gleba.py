from fastapi import Depends, HTTPException, APIRouter
from service import gleba_service
from schema import schemas
from database import get_db

router = APIRouter(prefix="/gleba")


@router.get('/', response_model=schemas.FeatureCollections)
async def get_glebas(skip: int = 0, limit: int = 100):
    return gleba_service.get_glebas(skip,limit)


@router.get('/{id}', response_model=schemas.Feature)
async def get(id:int):
    try:
        return gleba_service.get_gleba(id)
    except:
        raise HTTPException(404)
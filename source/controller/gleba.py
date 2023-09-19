from fastapi import Depends, HTTPException, APIRouter
from service import gleba_service
from schema import schemas
from database import get_db

router = APIRouter(prefix="/gleba")


@router.get('/', response_model=list[schemas.Gleba])
async def get_glebas():
    return gleba_service.get_glebas()


@router.get('/{id}', response_model=schemas.Gleba)
async def get(id:int):
    try:
        return gleba_service.get_gleba(id)
    except:
        raise HTTPException(404)
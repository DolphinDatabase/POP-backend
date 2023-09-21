from fastapi import Depends, HTTPException, APIRouter
from service import gleba_service
from schema import schemas
from model import Usuario
from typing import Annotated
from .auth_controller import get_current_user

router = APIRouter(prefix="/gleba")


@router.get('/', response_model=schemas.FeatureCollections)
async def get_glebas(user: Annotated[Usuario, Depends(get_current_user)],skip: int = 0, limit: int = 100):
    return gleba_service.get_glebas(skip,limit)


@router.get('/{id}', response_model=schemas.Feature)
async def get(id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    try:
        return gleba_service.get_gleba(id)
    except:
        raise HTTPException(404)
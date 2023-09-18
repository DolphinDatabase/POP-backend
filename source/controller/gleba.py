from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud.gleba as crud_gleba
from schema import schemas
from database import get_db

router = APIRouter(prefix="/gleba")

@router.get("/", response_model=list[schemas.Gleba])
def read_glebas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_gleba.get_glebas(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Gleba)
def read_glebas(id: int, db: Session = Depends(get_db)):
    result = crud_gleba.get_gleba(db, id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not found")
    return result

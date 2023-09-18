from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
from schema import schemas
from database import get_db

router = APIRouter(prefix="/gleba")

@router.get("/", response_model=list[schemas.Gleba])
async def read_operacaos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await crud.get_operacaos(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Gleba)
async def read_operacao(id: int, db: Session = Depends(get_db)):
    result = await crud.get_operacao(db, id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not found")
    return result

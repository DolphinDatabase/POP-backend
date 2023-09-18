
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import operacao as crud_operacao
from schema import schemas
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/operacao")

@router.get("/", response_model=list[schemas.Operacao])
def read_operacaos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operacaos = crud_operacao.get_operacaos(db, skip=skip, limit=limit)
    return operacaos


@router.get("/{id}", response_model=schemas.Operacao)
def read_operacao(id: int, db: Session = Depends(get_db)):
    result = crud_operacao.get_operacao(db, id=id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not found")
    return result
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import crud
from controller import schemas
from database import get_db
router = APIRouter(prefix='')


def configure_routes(app: FastAPI):
    @app.get("/operacao/", response_model=list[schemas.User])
    def read_operacaos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        operacaos = crud.get_operacaos(db, skip=skip, limit=limit)
        return operacaos

    @app.get("/operacao/{id}", response_model=schemas.User)
    def read_operacao(id: int, db: Session = Depends(get_db)):
        result = crud.get_operacao(db, id=id)
        if result is None:
            raise HTTPException(status_code=404, detail="Not found")
        return result

from fastapi import APIRouter,HTTPException
from datetime import date
from service import predict_mun

router = APIRouter(
    prefix="/time_series"
)

@router.get("/")
def get_time_series(gleba:int): 
    try:
        return predict_mun(gleba)
    except:
        raise HTTPException(404)

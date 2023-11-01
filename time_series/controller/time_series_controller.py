from fastapi import APIRouter,HTTPException
from datetime import date
from service import predict_mun, get_time_series

router = APIRouter(
    prefix="/time_series"
)
    
@router.get("/")
def get_data(gleba:int,inicio:str,fim:str): 
    try:
        data = get_time_series(gleba,inicio,fim)
        predict = predict_mun(gleba)
        return {'data':data['data'],'predict':predict['predicted_mean']}
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])

from fastapi import APIRouter,HTTPException
from datetime import date
from service import TimeSeriesService

router = APIRouter(
    prefix="/time_series"
)
    
@router.get("/")
def get_data(gleba:int,inicio:str,fim:str): 
    try:
        data = TimeSeriesService.get_time_series(gleba,inicio,fim)
        predict = TimeSeriesService.predict_mun(gleba)
        weather = TimeSeriesService.get_weather(gleba,fim)
        return {'data':data['data'],'predict':predict['predicted_mean'],'weather':weather}
    except Exception as e:
        raise HTTPException(status_code=e.args[0], detail=e.args[1])

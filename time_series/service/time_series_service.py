import joblib
import os
from datetime import date, datetime
import pandas as pd
import json
from cassandra.cluster import Cluster
from fastapi import HTTPException

def predict_mun(gleba:int):
    path = f'./model/{str(gleba)}.h5'
    if os.path.exists(path):
        model = joblib.load(path)
        forecast = model.get_forecast(steps=5)
        forecast = pd.DataFrame(forecast.predicted_mean)
        return json.loads(forecast.to_json())
    else:
        raise Exception(404,"No model")
    
def get_time_series(gleba:int,inicio:str,fim:str):
    cluster = Cluster(['localhost'])
    session = cluster.connect('prediction')
    query = f'SELECT * FROM data_series WHERE id_municipio={gleba}'
    rows = session.execute(query)
    data_series_list = [{"date":row.data,"data":row.valor_indice} for row in rows]
    if len(data_series_list) > 0:
        df = pd.DataFrame(data_series_list)
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
        df = df.set_index('date')
        df = df.groupby(df.index).mean()
        df = df.asfreq("W",method='backfill')
        df = df.sort_index()
        df = df.loc[datetime.strptime(inicio, "%Y-%m-%d"):datetime.strptime(fim, "%Y-%m-%d")]
        session.shutdown()
        cluster.shutdown()
        return json.loads(df.to_json())
    else:
        raise Exception(404,"No Gleba")
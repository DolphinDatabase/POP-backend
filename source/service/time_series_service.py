import joblib
import os
from datetime import date, datetime
import pandas as pd
import json
from cassandra.cluster import Cluster
from fastapi import HTTPException

class TimeSeriesService:

    @staticmethod
    def predict_mun(gleba:int):
        path = f'./source/ia_model/{str(gleba)}.h5'
        if os.path.exists(path):
            model = joblib.load(path)
            forecast = model.get_forecast(steps=10)
            forecast = pd.DataFrame(forecast.predicted_mean)
            return json.loads(forecast.to_json())
        else:
            raise Exception(404,"No model")
    
    @staticmethod
    def get_time_series(gleba:int,inicio:str,fim:str):
        cluster = Cluster(['localhost'])
        session = cluster.connect('prediction')
        query = f"SELECT * FROM data_series WHERE id_municipio={gleba} AND data > '{inicio}' AND data < '{fim}' ALLOW FILTERING"
        rows = session.execute(query)
        data_series_list = [{"date":row.data,"data":row.valor_indice} for row in rows]
        if len(data_series_list) > 0:
            df = pd.DataFrame(data_series_list)
            df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
            df = df.set_index('date')
            df = df.groupby(df.index).mean()
            df = df.sort_index()
            session.shutdown()
            cluster.shutdown()
            return json.loads(df.to_json())
        else:
            raise Exception(404,"No Gleba")
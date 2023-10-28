import joblib
import os
from datetime import date
import pandas as pd
import json

def predict_mun(gleba:int):
    path = f'./model/{str(gleba)}.h5'
    if os.path.exists(path):
        model = joblib.load(path)
        forecast = model.get_forecast(steps=5)
        forecast = pd.DataFrame(forecast.predicted_mean)
        return json.loads(forecast.to_json())
    else:
        raise Exception("No model")
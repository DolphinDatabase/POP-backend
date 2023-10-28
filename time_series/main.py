from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import controller

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(controller.time_series_router)

uvicorn.run(app=app, host="0.0.0.0",port=5000)
from fastapi import FastAPI 
import uvicorn
from database import Base, engine
from controller import termoController

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(termoController.router)

uvicorn.run(app=app, port=5050)

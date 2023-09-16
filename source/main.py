from fastapi import FastAPI 
from controller import auth_controller
import uvicorn


app = FastAPI()
auth_controller.configure(app)
uvicorn.run(app=app, port=5050)

from fastapi import FastAPI 
import controller
import uvicorn


app = FastAPI()

controller.user.configure_routes(app)

uvicorn.run(app=app, port=5050)

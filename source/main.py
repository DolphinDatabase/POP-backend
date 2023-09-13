from fastapi import FastApi 
import controller
import uvicorn


app = FastApi()

controller.user.configure_routes(app)

uvicorn.run(app=app, port=5050)

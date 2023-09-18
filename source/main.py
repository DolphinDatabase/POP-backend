from fastapi import FastAPI
import controller
import uvicorn
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(controller.termo_router)
app.include_router(controller.auth_router)
app.include_router(controller.usuario_router)
app.include_router(controller.historico_router)
app.include_router(controller.gleba_router)
app.include_router(controller.operacao_router)

uvicorn.run(app=app, port=5050)

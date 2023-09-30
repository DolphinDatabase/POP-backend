from fastapi import FastAPI
import controller
import uvicorn
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Base.metadata.create_all(engine)

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

app.include_router(controller.termo_router)
app.include_router(controller.auth_router)
app.include_router(controller.usuario_router)
app.include_router(controller.historico_router)
app.include_router(controller.gleba_router)
app.include_router(controller.operacao_router)

@app.get("/")
def home():
    return "Funcionando"

uvicorn.run(app=app, port=5050)

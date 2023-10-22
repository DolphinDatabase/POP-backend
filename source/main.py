from fastapi import FastAPI
import controller
import uvicorn
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi_redis_cache import RedisCache
from fastapi_cache import CacheControlMiddleware

redis_cache = RedisCache()

# Base.metadata.create_all(engine)

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    CacheControlMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
    cache=redis_cache
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

uvicorn.run(app=app, host="0.0.0.0",port=5050)

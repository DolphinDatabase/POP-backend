from fastapi import FastAPI, Request, Response
from sqlalchemy.orm import Session
import controller
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi_redis_cache import FastApiRedisCache, cache
import configuration
from cassandra.cluster import Cluster

# Base.metadata.create_all(engine)

app = FastAPI()
origins = ["*"]

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
app.include_router(controller.gleba_router)
app.include_router(controller.operacao_router)
app.include_router(controller.predicrion_router)


@app.get("/")
def home():
    return "Funcionando"


@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=configuration.REDIS_URL,
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session],
    )


uvicorn.run(app=app, host="0.0.0.0", port=5050)

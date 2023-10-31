from fastapi import FastAPI, Request, Response
from sqlalchemy.orm import Session
import controller
import uvicorn
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi_redis_cache import FastApiRedisCache, cache
import configuration
from cassandra.cluster import Cluster

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
app.include_router(controller.predicrion_router)

@app.get("/")
def home():
    return "Funcionando"

@app.on_event("startup")
def startup():
    cluster = Cluster([configuration.LOCAL_CASSANDRA_URL])
    session = cluster.connect()

    keyspace_query = "SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name = 'prediction'"
    keyspace_exists = session.execute(keyspace_query).one()

    if not keyspace_exists:
        create_keyspace_query = """
            CREATE KEYSPACE IF NOT EXISTS prediction
            WITH replication = {'class':'SimpleStrategy', 'replication_factor': 1}
        """
        session.execute(create_keyspace_query)

    session.set_keyspace("prediction")

    table_query = "SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'prediction' AND table_name = 'data_series'"
    table_exists = session.execute(table_query).one()

    if not table_exists:
        create_table_query = """
            CREATE TABLE data_series (
                id_municipio INT,
                data_id UUID,
                valor_indice FLOAT,
                data TEXT,
                PRIMARY KEY (id_municipio, data_id)
            ) WITH CLUSTERING ORDER BY (data_id ASC);
        """
        session.execute(create_table_query)

    session.shutdown()
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url= configuration.LOCAL_REDIS_URL,
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )

uvicorn.run(app=app, host="0.0.0.0",port=5050)

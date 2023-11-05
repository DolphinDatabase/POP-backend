from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import controller
from cassandra.cluster import Cluster

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

@app.on_event("startup")
def startup():
    cluster = Cluster(['localhost'])
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
                data DATE,
                PRIMARY KEY (id_municipio, data_id)
            ) WITH CLUSTERING ORDER BY (data DESC, data_id ASC);
        """
        session.execute(create_table_query)


app.include_router(controller.time_series_router)

uvicorn.run(app=app, host="0.0.0.0",port=5000)
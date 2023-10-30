import uuid
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from cassandra.cluster import Cluster

router = APIRouter(prefix="/prediction")

class DataSeries(BaseModel):
    id_municipio: int
    valor_indice: float
    data: str

@router.post("/create/")
async def create_data_series(data_series: DataSeries):
    try:
        cluster = Cluster(['localhost'])
        session = cluster.connect('prediction')
        query = "INSERT INTO data_series (data_id, id_municipio, valor_indice, data) VALUES (%s, %s, %s, %s)"
        session.execute(query, (uuid.uuid4(), data_series.id_municipio, data_series.valor_indice, data_series.data))
        return {"message": "Registro criado com sucesso"}
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail=f"Erro: {e}, Erro ao criar o registro")
    finally:
        session.shutdown()
        cluster.shutdown()

@router.get("/list/")
async def list_data_series():
    try:
        cluster = Cluster(['localhost'])
        session = cluster.connect('prediction')

        query = "SELECT * FROM data_series"
        rows = session.execute(query)
        data_series_list = [{"data_id": row.data_id, "id_municipio": row.id_municipio, "valor_indice": row.valor_indice, "data": row.data} for row in rows]
        return data_series_list
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail=f"Erro: {e}, Erro ao listar registros")
    finally:
        session.shutdown()
        cluster.shutdown()

@router.get("/get/{data_id}")
async def get_data_series(data_id: str):
    try:
        cluster = Cluster(['localhost'])
        session = cluster.connect('prediction')

        query = "SELECT * FROM data_series WHERE data_id = %s ALLOW FILTERING"
        row = session.execute(query, (uuid.UUID(data_id),)).one()
        if row:
            return {"data_id": row.data_id, "id_municipio": row.id_municipio, "valor_indice": row.valor_indice, "data": row.data}
        else:
            raise HTTPException(status_code=404, detail="Registro não encontrado")
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail=f"Erro: {e}, Erro ao buscar registro")
    finally:
        session.shutdown()
        cluster.shutdown()

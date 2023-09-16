from database import SessionLocal
from model.historico import Historico
from schema.historicoSchema import HistoricoBase
from datetime import date

def create_historico(historico:HistoricoBase):
    db = SessionLocal()
    h = Historico(usuario_id=historico.usuario.id,termo_id=historico.termo.id,data=date.today())
    db.add(h)
    db.commit()
    db.refresh(h)
    db.close()
    return h
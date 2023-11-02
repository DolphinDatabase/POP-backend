from database import SessionLocal
from model import Historico
from schema import CreateHistorico
from datetime import date

class HistoricoService:
    def create_historico(historico:CreateHistorico):
        db = SessionLocal()
        h = Historico(usuario_id=historico.usuario,termo_id=historico.termo,data=date.today())
        db.add(h)
        db.commit()
        db.refresh(h)
        db.close()
        return h
    
    def get_historico_by_user(usuario:int):
        db = SessionLocal()
        h = db.query(Historico).where(Historico.usuario_id == usuario).order_by(Historico.data)
        db.close()
        return h
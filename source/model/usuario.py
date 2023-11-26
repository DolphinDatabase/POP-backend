from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = "usr_usuario"

    id = Column("usr_id", Integer, primary_key=True, index=True)
    nome = Column("usr_nome", String(150))
    doc = Column("usr_doc", String(14))
    email = Column("usr_email", String(255), unique=True)
    senha = Column("usr_senha", String(255))
    grupo = Column("usr_grupo", String(25))
    ativo = Column("usr_ativo", Boolean)

    def as_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "doc": self.doc,
            "email": self.email,
            "senha": self.senha,
            "grupo": self.grupo,
            "ativo": self.ativo,
        }

    @staticmethod
    def from_dict(usuario_dict):
        usuario = Usuario()
        usuario.id = usuario_dict["id"]
        usuario.nome = usuario_dict["nome"]
        usuario.doc = usuario_dict["doc"]
        usuario.email = usuario_dict["email"]
        usuario.senha = usuario_dict["senha"]
        usuario.grupo = usuario_dict["grupo"]
        usuario.ativo = usuario_dict["ativo"]
        return usuario

from typing import List

from controller.exceptions import object_not_found_exception
from database import SessionLocal
from model import Termo, Usuario, Condicao, Grupo, Servico
from model.aceite import TermoAceite, CondicaoAceite
from schema import BaseTermo
from datetime import datetime
from sqlalchemy import desc

from schema.termo_schema import AcceptTermo
from .usuario_service import UsuarioService


class TermoService:
    @staticmethod
    def create_termo(novo_termo: BaseTermo) -> Termo:
        with SessionLocal() as db:
            termo = Termo(
                data=datetime.now(),
                grupo=novo_termo.grupo.value,
                texto=novo_termo.texto,
            )

            for condicao in novo_termo.condicoes:
                servico = None if condicao.servico is None else condicao.servico.value
                condicao = Condicao(texto=condicao.texto, servico=servico)

                termo.condicoes.append(condicao)

            db.add(termo)
            db.commit()
            db.refresh(termo)

        return termo

    @staticmethod
    def list_termo() -> List[Termo]:
        with SessionLocal() as db:
            termos = db.query(Termo).all()
        return termos

    @staticmethod
    def get_last_termo_aceite(usuario: Usuario):
        with SessionLocal() as db:
            termo = (
                db.query(Termo)
                .where(Termo.grupo == usuario.grupo)
                .order_by(desc(Termo.data))
                .first()
            )

            if termo is None:
                raise object_not_found_exception

            termo.aceite = usuario.id in [aceite.usuario.id for aceite in termo.aceites if aceite.aceite]

            for condicao in termo.condicoes:
                condicao.aceite = usuario.id in [aceite.usuario.id for aceite in condicao.aceites if aceite.aceite]

        return termo

    @staticmethod
    def accept_termo(usuario: Usuario, novo_termo_aceite: AcceptTermo) -> AcceptTermo:
        with SessionLocal() as db:
            termo = (
                db.query(Termo)
                .where(Termo.grupo == usuario.grupo)
                .order_by(desc(Termo.data))
                .first()
            )

            if termo.id != novo_termo_aceite.id:
                raise object_not_found_exception

            termo_aceite = TermoAceite(
                termo_id=termo.id,
                usuario_id=usuario.id,
                aceite=novo_termo_aceite.aceite,
                data=datetime.now(),
            )

            for novo_condicao_aceite in novo_termo_aceite.condicoes:
                condicao = (
                    db.query(Condicao)
                    .where(
                        Condicao.termo_id == termo.id,
                        Condicao.id == novo_condicao_aceite.id,
                    )
                    .first()
                )

                if condicao is None:
                    raise object_not_found_exception

                condicao_aceite = CondicaoAceite(
                    condicao_id=condicao.id,
                    usuario_id=usuario.id,
                    aceite=novo_condicao_aceite.aceite,
                    data=datetime.now(),
                )

                db.add(condicao_aceite)
            db.add(termo_aceite)

            if termo_aceite.aceite:
                UsuarioService().active_user(usuario)

            db.commit()

        return novo_termo_aceite

    @staticmethod
    def get_last_termo_by_grupo(grupo: Grupo) -> Termo:
        with SessionLocal() as db:
            termo = (
                db.query(Termo)
                .where(Termo.grupo == grupo.value)
                .order_by(desc(Termo.data))
                .first()
            )

        return termo

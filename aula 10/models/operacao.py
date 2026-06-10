from datetime import datetime

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"

    id = db.column(db.Integer, primary_key=True)
    num1 = db.column(db.Float, nullable=False)
    num2 = db.column(db.Float, nullable=True)
    operacao = db.column(db.String(10), nullable=True)
    etapas = db.column(db.String(255), nullable=True)
    resultado  = db.column(db.String(100), nullable=True)
    criado_em = db.column(db.DateTime, default=datetime.now)

    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
        )
        db.session.add(registro)
        db.session.commit()
        return registro

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"

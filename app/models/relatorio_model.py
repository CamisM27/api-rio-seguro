from sqlalchemy import Column, Integer, DateTime, ForeignKey, LargeBinary
from app.database import Base


class Relatorio(Base):

    __tablename__ = "tbl_relatorios"

    id_relatorio = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_relatorio = Column(
        DateTime,
        nullable=False
    )

    caminho = Column(
        LargeBinary,
        nullable=False
    )

    id_usuario = Column(
        Integer,
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )
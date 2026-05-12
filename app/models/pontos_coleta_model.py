from sqlalchemy import Column, Integer, String, Text,  DECIMAL
from app.database import Base


class PontoColeta(Base):

    __tablename__ = "tbl_pontos_coleta"

    id_ponto = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    descricao = Column(
        Text,
        nullable=False
    )

    latitude = Column(
        DECIMAL(10, 8)
    )

    longitude = Column(
        DECIMAL(11, 8)
    )

    rio = Column(
        String(100),
        nullable=False
    )

    comunidade = Column(
        String(100),
        nullable=False
    )
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, LargeBinary
from app.database import Base


class RegistroPescador(Base):

    __tablename__ = "tbl_registro_pescador"

    id_registro = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_registro = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    cor_agua = Column(
        String(20),
        nullable=False
    )

    odor = Column(
        Boolean,
        nullable=False
    )

    chuva_ultimos_dias = Column(
        Boolean,
        nullable=False
    )

    chuva_24h = Column(
        Boolean,
        nullable=False
    )

    nome_local = Column(
        String(100),
        nullable=False
    )

    foto = Column(LargeBinary)

    temperatura = Column(
        String(30),
        nullable=False
    )

    id_usuario = Column(
        Integer,
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )
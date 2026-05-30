from sqlalchemy import (Column, Integer, String, Float, DateTime, ForeignKey)

from app.database import Base


class RegistroTeste(Base):

    __tablename__ = "tbl_registro_teste"

    id_teste = Column(Integer, primary_key=True, autoincrement=True)

    data_teste = Column(
        DateTime,
        nullable=False
    )

    transparencia_agua = Column(
        Float,
        nullable=False
    )

    espuma = Column(
        String(50),
        nullable=False
    )

    residuos_margem = Column(
        String(50),
        nullable=False
    )

    odor = Column(
        String(50),
        nullable=False
    )

    material_sedimentavel = Column(
        String(30),
        nullable=False
    )

    peixes = Column(String(20))

    larvas_vermes_vermelhos = Column(
        String(20)
    )

    larvas_vermes_conchas = Column(
        String(20)
    )

    coliformes = Column(Float)

    oxigenio_od1 = Column(Float)

    oxigenio_od5 = Column(Float)

    potencial_hidrogenionico = Column(
        Float,
        nullable=False
    )

    nitrato = Column(Float)

    fosfatos = Column(Float)

    pontuacao_total = Column(Integer)

    qualidade_agua = Column(String(20))

    id_usuario = Column(
        Integer,
        ForeignKey(
            "tbl_usuario.id_usuario"
        ),
        nullable=False
    )

    id_ponto = Column(
        Integer,
        ForeignKey(
            "tbl_pontos_coleta.id_ponto"
        ),
        nullable=False
    )
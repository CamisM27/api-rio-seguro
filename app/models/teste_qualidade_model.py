from sqlalchemy import (Column, Integer, String, DateTime,  ForeignKey)

from app.database import Base


class RegistroTeste(Base):

    __tablename__ = "tbl_registro_teste"

    id_teste = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_teste = Column(
        DateTime,
        nullable=False
    )

    transparencia_agua = Column(
        Integer,
        nullable=False
    )

    espuma = Column(
        String(50),
        nullable=False
    )

    residuos_margem = Column(
        String(70),
        nullable=False
    )

    odor = Column(
        String(50),
        nullable=False
    )

    material_sedimentavel = Column(
        String(20),
        nullable=False
    )

    peixes = Column(
        String(20)
    )

    larvas_vermes_vermelhos = Column(
        String(10)
    )

    larvas_vermes_conchas = Column(
        String(10)
    )

    coliformes = Column(
        Integer
    )

    oxigenio_od1 = Column(
        Integer
    )

    oxigenio_od5 = Column(
        Integer
    )

    potencial_hidrogenionico = Column(
        Integer
    )

    nitrato = Column(
        Integer
    )

    fosfatos = Column(
        Integer
    )
    pontuacao_total = Column(Integer)

    qualidade_agua = Column(String(20))
    
    id_usuario = Column(
        Integer,
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )

    id_ponto = Column(
        Integer,
        ForeignKey("tbl_pontos_coleta.id_ponto"),
        nullable=False
    )
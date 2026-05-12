from sqlalchemy import Column, Integer, String, Date, LargeBinary
from app.database import Base

class Usuario(Base):
    __tablename__ = "tbl_usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)

    nome = Column(String(100), nullable=False)

    data_nascimento = Column(Date, nullable=False)

    telefone = Column(String(20))

    email = Column(String(100))

    foto_perfil = Column(LargeBinary)

    tipo_usuario = Column(String(50))
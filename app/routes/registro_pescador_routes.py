from fastapi import APIRouter, Depends
import database

router = APIRouter(
    prefix="/api/v1/pescadores",
    tags=["Registro de Pescadores"]
)

@router.get("/")
def listar_pescadores(db = Depends(database)):
    # Query para listar pescadores cadastrados
    return {
        "mensagem": "Retorna lista de pescadores registrados"
    }

@router.post("/")
def registrar_pescadores(pescador: dict, db = Depends(database)):
    # Logica para cadastrar pescador novo
    return {
        "mensagem": "Pescador registrado com sucesso"
    }

@router.delete("/{id_pescador}")
def remover_pescador(id_pescador: int, db = Depends(database)):
    # Query para apagar pescadores por id
    return{
        "mensagem": f"Registro do pescador {id_pescador} removido"
    }
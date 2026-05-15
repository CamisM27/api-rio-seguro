from fastapi import APIRouter, Depends
import database 

router = APIRouter(
    prefix="/api/v1/pontos-coleta",
    tags=["Pontos de Coleta"]
)

@router.get("/")
def listar_pontos(db = Depends(database)):
    # Query para listar todos os pontos de coleta cadastrados
    return {
        "mensagem": "Retorna todos os pontos de coleta geográficos"
    }

@router.post("/")
def criar_ponto(ponto: dict, db = Depends(database)):
    # Logica para criar ponto
    return {
        "mensagem": "Novo ponto de coleta adicionado"
    }
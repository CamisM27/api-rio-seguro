from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.auth_dependency import (
    usuario_autenticado
)

from app.schema.teste_qualidade_schema import (
    RegistroTesteCreate,
    RegistroTesteResponse,
    RegistroTesteUpdate
)

from app.services.teste_qualidade_service import (
    criar_registro_teste,
    atualizar_registro_teste,
    deletar_registro_teste,
    listar_registros_teste,
    visualizar_registro_teste
)

router = APIRouter(
    prefix="/registro-teste",
    tags=["Registro Teste"],
    dependencies=[
        Depends(usuario_autenticado)
    ]
)


@router.get(
    "/",
    response_model=list[RegistroTesteResponse]
)
def listar_relatorios(
    db: Session = Depends(get_db)
):

    return listar_registros_teste(
        db
    )


@router.get(
    "/{id_teste}",
    response_model=RegistroTesteResponse
)
def visualizar_relatorio(
    id_teste: int,
    db: Session = Depends(get_db)
):

    return visualizar_registro_teste(
        db,
        id_teste
    )


@router.post(
    "/",
    response_model=RegistroTesteResponse
)
def cadastrar_registro(
    registro_data: RegistroTesteCreate,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):
    return criar_registro_teste(
    db,
    registro_data,
    usuario_logado
    )


@router.put(
    "/{registro_id}",
    response_model=RegistroTesteResponse
)
def atualizar_registro(
    registro_id: int,
    registro_data: RegistroTesteUpdate,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):
    return atualizar_registro_teste(
        db,
        registro_id,
        registro_data,
        usuario_logado
    )


@router.delete(
    "/{registro_id}"
)
def deletar_registro(
    registro_id: int,
    db: Session = Depends(get_db)
):

    return deletar_registro_teste(
        db,
        registro_id
    )
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException

from app.models.teste_qualidade_model import (
    RegistroTeste
)
from app.schema.teste_qualidade_schema import (
    RegistroTesteCreate,
    RegistroTesteUpdate
)

def deletar_registro_teste(
    db: Session,
    id_teste: int
):

    registro = db.query(
        RegistroTeste
    ).filter(
        RegistroTeste.id_teste == id_teste
    ).first()

    if not registro:

        raise HTTPException(
            status_code=404,
            detail="Registro não encontrado"
        )

    limite_exclusao = (
        registro.data_teste
        + timedelta(days=7)
    )

    if datetime.utcnow() > limite_exclusao:

        raise HTTPException(
            status_code=403,
            detail=(
                "O prazo de 7 dias "
                "para exclusão expirou"
            )
        )

    db.delete(registro)

    db.commit()

    return {
        "message":
        "Registro deletado com sucesso"
    }


def classificar_qualidade(
    pontuacao: float
):

    if pontuacao <= 20:
        return "Péssima"

    elif pontuacao <= 26:
        return "Ruim"

    elif pontuacao <= 35:
        return "Regular"

    elif pontuacao <= 40:
        return "Boa"

    return "Ótima"

def atualizar_registro_teste(
    db: Session,
    id_teste: int,
    registro_update: RegistroTesteUpdate
):

    registro = db.query(
        RegistroTeste
    ).filter(
        RegistroTeste.id_teste == id_teste
    ).first()

    if not registro:

        raise HTTPException(
            status_code=404,
            detail="Registro não encontrado"
        )

    limite_edicao = (
        registro.data_teste
        + timedelta(days=7)
    )

    if datetime.utcnow() > limite_edicao:

        raise HTTPException(
            status_code=403,
            detail=(
                "O prazo de 7 dias "
                "para atualização expirou"
            )
        )

    dados_update = registro_update.model_dump(
        exclude_unset=True
    )

    for chave, valor in dados_update.items():

        setattr(
            registro,
            chave,
            valor
        )

    parametros = [

        registro.transparencia_agua,

        registro.coliformes,

        registro.oxigenio_od1,

        registro.oxigenio_od5,

        registro.potencial_hidrogenionico,

        registro.nitrato,

        registro.fosfatos
    ]

    soma = sum(
        p for p in parametros
        if p is not None
    )

    quantidade = len(
        [
            p for p in parametros
            if p is not None
        ]
    )

    media = soma / quantidade

    pontuacao_final = round(
        media * 14
    )

    qualidade = classificar_qualidade(
        pontuacao_final
    )

    registro.pontuacao_total = pontuacao_final
    registro.qualidade_agua = qualidade

    db.commit()

    db.refresh(registro)

    return registro


def criar_registro_teste(
    db: Session,
    registro_data: RegistroTesteCreate
):

    parametros = [

        registro_data.transparencia_agua,

        registro_data.coliformes,

        registro_data.oxigenio_od1,

        registro_data.oxigenio_od5,

        registro_data.potencial_hidrogenionico,

        registro_data.nitrato,

        registro_data.fosfatos
    ]

    soma = sum(
        p for p in parametros
        if p is not None
    )

    quantidade = len(
        [
            p for p in parametros
            if p is not None
        ]
    )

    media = soma / quantidade

    pontuacao_final = round(
        media * 14
    )

    qualidade = classificar_qualidade(
        pontuacao_final
    )

    novo_registro = RegistroTeste(

        data_teste=registro_data.data_teste,

        transparencia_agua=registro_data.transparencia_agua,

        espuma=registro_data.espuma,

        residuos_margem=registro_data.residuos_margem,

        odor=registro_data.odor,

        material_sedimentavel=registro_data.material_sedimentavel,

        peixes=registro_data.peixes,

        larvas_vermes_vermelhos=registro_data.larvas_vermes_vermelhos,

        larvas_vermes_conchas=registro_data.larvas_vermes_conchas,

        coliformes=registro_data.coliformes,

        oxigenio_od1=registro_data.oxigenio_od1,

        oxigenio_od5=registro_data.oxigenio_od5,

        potencial_hidrogenionico=registro_data.potencial_hidrogenionico,

        nitrato=registro_data.nitrato,

        fosfatos=registro_data.fosfatos,

        pontuacao_total=pontuacao_final,

        qualidade_agua=qualidade,

        id_usuario=registro_data.id_usuario,

        id_ponto=registro_data.id_ponto
    )

    db.add(novo_registro)

    db.commit()

    db.refresh(novo_registro)

    return novo_registro

def listar_registros_teste(
    db: Session
):

    registros = db.query(
        RegistroTeste
    ).all()

    return registros


def visualizar_registro_teste(
    db: Session,
    id_teste: int
):

    registro = db.query(
        RegistroTeste
    ).filter(
        RegistroTeste.id_teste == id_teste
    ).first()

    if not registro:

        raise HTTPException(
            status_code=404,
            detail="Relatório não encontrado"
        )

    return registro
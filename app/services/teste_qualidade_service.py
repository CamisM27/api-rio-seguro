from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuario_model import Usuario
from app.models.pontos_coleta_model import PontoColeta
from app.models.teste_qualidade_model import RegistroTeste
from app.schema.teste_qualidade_schema import RegistroTesteCreate, RegistroTesteUpdate


def classificar_qualidade(pontuacao: int):

    if pontuacao <= 20:
        return "Péssima"

    elif pontuacao <= 26:
        return "Ruim"

    elif pontuacao <= 35:
        return "Regular"

    elif pontuacao <= 40:
        return "Boa"

    return "Ótima"


def calcular_transparencia(valor: float):

    if (41 <= valor <= 100):
        return 2

    elif valor > 100:
        return 1
    
    elif valor < 40:
        return 3


def calcular_espuma(valor: str):

    mapa = {
        "Grande quantidade, formando flocos": 1,
        "Pouca quantidade": 2,
        "Ausente": 3
    }

    return mapa[valor]


def calcular_residuos_margem(valor: str):

    mapa = {
        "Muito resíduo": 1,
        "Pouco resíduo": 2,
        "Nenhum": 3
    }

    return mapa[valor]


def calcular_odor(valor: str):

    mapa = {
        "Fétido ou cheiro de ovo podre": 1,
        "Fraco de mofo ou de capim": 2,
        "Nenhum": 3
    }

    return mapa[valor]


def calcular_material_sedimentavel(valor: str):

    mapa = {
        "Muito alto": 1,
        "Baixo": 2,
        "Ausente": 3
    }

    return mapa[valor]


def calcular_peixes(valor: str):

    mapa = {
        "Nenhum": 1,
        "Poucos": 2,
        "Muitos": 3
    }

    return mapa[valor]


def calcular_larvas_vermelhas(valor: str):

    mapa = {
        "Muitos": 1,
        "Poucos": 2,
        "Nenhum": 3
    }

    return mapa[valor]


def calcular_larvas_conchas(valor: str):

    mapa = {
        "Nenhum": 1,
        "Raros": 2,
        "Frequentes": 3
    }

    return mapa[valor]


def calcular_coliformes(valor: float):

    if valor > 500:
        return 1

    elif valor > 200:
        return 2

    return 3


def calcular_od1(valor: float):

    if valor <= 4:
        return 1

    elif valor <= 6:
        return 2

    return 3


def calcular_od5(od1: float, od5: float):

    dbo = od1 - od5

    if dbo > 8:
        return 1

    elif dbo > 4:
        return 2

    return 3


def calcular_ph(valor: float):

    if valor > 9 or valor < 5:
        return 1

    elif 5 <= valor <= 6 or 7.1 <= valor <= 9:
        return 2

    return 3


def calcular_nitrato(valor: float):

    if valor > 20:
        return 1

    elif valor > 5:
        return 2

    return 3


def calcular_fosfato(valor: float):

    if valor > 2:
        return 1

    elif valor > 1:
        return 2

    return 3


def calcular_pontuacao(registro):

    parametros = [
        calcular_transparencia(registro.transparencia_agua),
        calcular_espuma(registro.espuma),
        calcular_residuos_margem(registro.residuos_margem),
        calcular_odor(registro.odor),
        calcular_material_sedimentavel(registro.material_sedimentavel),
        calcular_ph(registro.potencial_hidrogenionico)
    ]

    if registro.peixes is not None:
        parametros.append(
            calcular_peixes(registro.peixes)
        )

    if registro.larvas_vermes_vermelhos is not None:
        parametros.append(
            calcular_larvas_vermelhas(
                registro.larvas_vermes_vermelhos
            )
        )

    if registro.larvas_vermes_conchas is not None:
        parametros.append(
            calcular_larvas_conchas(
                registro.larvas_vermes_conchas
            )
        )

    if registro.coliformes is not None:
        parametros.append(
            calcular_coliformes(
                registro.coliformes
            )
        )

    if registro.oxigenio_od1 is not None:
        parametros.append(
            calcular_od1(
                registro.oxigenio_od1
            )
        )

    if (
        registro.oxigenio_od1 is not None
        and registro.oxigenio_od5 is not None
    ):

        parametros.append(
            calcular_od5(
                registro.oxigenio_od1,
                registro.oxigenio_od5
            )
        )

    if registro.nitrato is not None:
        parametros.append(
            calcular_nitrato(
                registro.nitrato
            )
        )

    if registro.fosfatos is not None:
        parametros.append(
            calcular_fosfato(
                registro.fosfatos
            )
        )

    media = sum(parametros) / len(parametros)

    if len(parametros) < 14:

        pontuacao = round(
            media * 14
        )

    else:

        pontuacao = sum(
            parametros
        )

    qualidade = classificar_qualidade(
        pontuacao
    )

    return pontuacao, qualidade


def buscar_registro_ou_404(db: Session, id_teste: int):

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

    return registro


def validar_usuario_e_ponto(db: Session, id_usuario: int, id_ponto: int):

    usuario = db.query(
        Usuario
    ).filter(
        Usuario.id_usuario == id_usuario
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    if not usuario.ativo:

        raise HTTPException(
            status_code=403,
            detail="Usuário desativado"
        )

    ponto = db.query(
        PontoColeta
    ).filter(
        PontoColeta.id_ponto == id_ponto
    ).first()

    if not ponto:

        raise HTTPException(
            status_code=404,
            detail="Ponto de coleta não encontrado"
        )


def validar_limite_7_dias(data_teste: datetime, operacao: str):

    limite = data_teste + timedelta(days=7)

    if datetime.utcnow() > limite:

        raise HTTPException(
            status_code=403,
            detail=f"O prazo de 7 dias para {operacao} expirou"
        )


def criar_registro_teste(db: Session, registro_data: RegistroTesteCreate, usuario_logado: dict):

    id_usuario = usuario_logado["id_usuario"]

    validar_usuario_e_ponto(
        db,
        id_usuario,
        registro_data.id_ponto
    )

    pontuacao, qualidade = calcular_pontuacao(
        registro_data
    )

    novo_registro = RegistroTeste(
        **registro_data.model_dump(),
        pontuacao_total=pontuacao,
        qualidade_agua=qualidade,
        id_usuario=id_usuario
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro


def listar_registros_teste(db: Session):

    return db.query(
        RegistroTeste
    ).all()


def visualizar_registro_teste(db: Session, id_teste: int):

    return buscar_registro_ou_404(
        db,
        id_teste
    )


def atualizar_registro_teste(
    db: Session,
    id_teste: int,
    registro_update: RegistroTesteUpdate,
    usuario_logado: dict
):

    registro = buscar_registro_ou_404(
        db,
        id_teste
    )

    validar_limite_7_dias(
        registro.data_teste,
        "atualização"
    )

    for chave, valor in registro_update.model_dump(
        exclude_unset=True
    ).items():

        setattr(
            registro,
            chave,
            valor
        )

    pontuacao, qualidade = calcular_pontuacao(
        registro
    )

    registro.pontuacao_total = pontuacao
    registro.qualidade_agua = qualidade

    db.commit()
    db.refresh(registro)

    return registro


def deletar_registro_teste(db: Session, id_teste: int):

    registro = buscar_registro_ou_404(
        db,
        id_teste
    )

    validar_limite_7_dias(
        registro.data_teste,
        "exclusão"
    )

    db.delete(registro)
    db.commit()

    return {
        "message":
        "Registro deletado com sucesso"
    }
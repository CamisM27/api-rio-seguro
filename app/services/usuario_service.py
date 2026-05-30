from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import UploadFile
from app.models.usuario_model import Usuario
from app.schema.usuario_schema import UsuarioCreate
from fastapi.responses import Response

def listar_usuarios_service(
    db: Session
):

    return db.query(
        Usuario
    ).filter(
        Usuario.ativo == True
    ).all()

def criar_usuario_service(
    db: Session,
    usuario_data: UsuarioCreate
):

    usuario_existente = db.query(
        Usuario
    ).filter(
        Usuario.email == usuario_data.email
    ).first()

    if usuario_existente:

        raise HTTPException(
            status_code=409,
            detail="Já existe um usuário com este email"
        )

    novo_usuario = Usuario(

        nome=usuario_data.nome,
        data_nascimento=usuario_data.data_nascimento,
        telefone=usuario_data.telefone,
        email=usuario_data.email,
        tipo_usuario=usuario_data.tipo_usuario,
        foto_perfil=usuario_data.foto_perfil,
        ativo=True
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

def obter_usuario_por_id_service(
    db: Session,
    id_usuario: int
):

    usuario = db.query(
        Usuario
    ).filter(
        Usuario.id_usuario == id_usuario,
        Usuario.ativo == True
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario

def desativar_usuario_service(
    db: Session,
    id_usuario: int
):

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
            status_code=400,
            detail="Usuário já está desativado"
        )

    usuario.ativo = False

    db.commit()
    return usuario

async def atualizar_foto_usuario_service(
    db: Session,
    id_usuario: int,
    foto: UploadFile
):

    usuario = db.query(
        Usuario
    ).filter(
        Usuario.id_usuario == id_usuario,
        Usuario.ativo == True
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    extensoes_permitidas = [
        "image/png",
        "image/jpeg",
        "image/jpg"
    ]

    if foto.content_type not in extensoes_permitidas:

        raise HTTPException(
            status_code=400,
            detail=(
                "Formato inválido. "
                "Use PNG ou JPG"
            )
        )

    usuario.foto_perfil = await foto.read()

    db.commit()

    return {
        "id_usuario":
        usuario.id_usuario
    }

def visualizar_foto_usuario_service(
    db: Session,
    id_usuario: int
):

    usuario = db.query(
        Usuario
    ).filter(
        Usuario.id_usuario == id_usuario,
        Usuario.ativo == True
    ).first()

    if not usuario:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    if not usuario.foto_perfil:

        raise HTTPException(
            status_code=404,
            detail="Usuário não possui foto"
        )

    return Response(
        content=usuario.foto_perfil,
        media_type="image/jpeg"
    )
def reativar_usuario_service(
    db: Session,
    id_usuario: int
):

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

    if usuario.ativo:

        raise HTTPException(
            status_code=400,
            detail="Usuário já está ativo"
        )

    usuario.ativo = True

    db.commit()

    db.refresh(usuario)

    return usuario
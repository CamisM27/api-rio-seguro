from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class EspumaEnum(str, Enum):

    grande_quantidade = "Grande quantidade, formando flocos"
    pouca_quantidade = "Pouca quantidade"
    ausente = "Ausente"


class ResiduosMargemEnum(str, Enum):

    muito_residuo = "Muito resíduo"
    pouco_residuo = "Pouco resíduo"
    nenhum = "Nenhum"


class OdorEnum(str, Enum):

    fetido = "Fétido ou cheiro de ovo podre"
    fraco = "Fraco de mofo ou de capim"
    nenhum = "Nenhum"


class MaterialSedimentavelEnum(str, Enum):

    muito_alto = "Muito alto"
    baixo = "Baixo"
    ausente = "Ausente"


class PeixesEnum(str, Enum):

    nenhum = "Nenhum"
    poucos = "Poucos"
    muitos = "Muitos"


class LarvasVermelhasEnum(str, Enum):

    muitos = "Muitos"
    poucos = "Poucos"
    nenhum = "Nenhum"


class LarvasConchasEnum(str, Enum):

    nenhum = "Nenhum"
    raros = "Raros"
    frequentes = "Frequentes"


class RegistroTesteBase(BaseModel):

    data_teste: datetime
    transparencia_agua: float
    espuma: EspumaEnum
    residuos_margem: ResiduosMargemEnum
    odor: OdorEnum
    material_sedimentavel: MaterialSedimentavelEnum
    peixes: Optional[PeixesEnum] = None
    larvas_vermes_vermelhos: Optional[LarvasVermelhasEnum] = None
    larvas_vermes_conchas: Optional[LarvasConchasEnum] = None
    coliformes: Optional[float] = None
    oxigenio_od1: Optional[float] = None
    oxigenio_od5: Optional[float] = None
    potencial_hidrogenionico: float
    nitrato: Optional[float] = None
    fosfatos: Optional[float] = None
    id_ponto: int


class RegistroTesteCreate(
    RegistroTesteBase
):
    pass


class RegistroTesteUpdate(
    BaseModel
):

    data_teste: Optional[datetime] = None
    transparencia_agua: Optional[float] = None
    espuma: Optional[EspumaEnum] = None
    residuos_margem: Optional[ResiduosMargemEnum] = None
    odor: Optional[OdorEnum] = None
    material_sedimentavel: Optional[MaterialSedimentavelEnum] = None
    peixes: Optional[PeixesEnum] = None
    larvas_vermes_vermelhos: Optional[LarvasVermelhasEnum] = None
    larvas_vermes_conchas: Optional[LarvasConchasEnum] = None
    coliformes: Optional[float] = None
    oxigenio_od1: Optional[float] = None
    oxigenio_od5: Optional[float] = None
    potencial_hidrogenionico: Optional[float] = None
    nitrato: Optional[float] = None
    fosfatos: Optional[float] = None
    id_ponto: Optional[int] = None


class RegistroTesteResponse(
    RegistroTesteBase
):

    id_teste: int
    pontuacao_total: int
    qualidade_agua: str
    id_usuario: int

    class Config:

        from_attributes = True
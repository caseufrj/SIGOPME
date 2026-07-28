from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ProtocoloRastreabilidade:
    protocolo: int

    registro: str = ""
    paciente: str = ""

    licitacao: str = ""
    codigo_item: str = ""
    nome_material: str = ""
    lote: str = ""
    serie: str = ""
    codigo_barras: str = ""

    data_retirada: Optional[datetime] = None
    data_utilizacao: Optional[datetime] = None
    data_devolucao: Optional[datetime] = None

    status: str = ""

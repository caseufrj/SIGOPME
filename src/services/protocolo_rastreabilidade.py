from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProtocoloRastreabilidade:
    protocolo: int

    registro: str
    paciente: str

    licitacao: str
    codigo_item: str
    nome_material: str
    lote: str
    serie: str
    codigo_barras: str

    data_retirada: datetime | None = None
    data_utilizacao: datetime | None = None
    data_devolucao: datetime | None = None

    status: str = ""

from enum import Enum
from pydantic import BaseModel

class Categoria(Enum):
    INDEFINIDO = 0
    FAMILIA = 1
    AMIGO = 2
    COMERCIAL = 3
    OUTROS = 4

class TipoTelefone(Enum):
    INDEFINIDO = 0
    MOVEL = 1
    FIXO = 2
    COMERCIAL = 3

class Contato(BaseModel):
    id: int
    nome: str
    telefone: str
    tipoTelefone: TipoTelefone
    categoria: Categoria
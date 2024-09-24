from typing import List

from pydantic import BaseModel

from .Operacao import Operacao
from .Bem import Bem


class Garantia(BaseModel):
    codigoGarantia: str
    operacoes: List[Operacao]
    bens: List[Bem]
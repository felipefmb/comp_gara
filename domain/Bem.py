from typing import List

from pydantic import BaseModel

from .Garantidor import Garantidor


class Bem(BaseModel):
    codigoBem: str
    garantidores: List[Garantidor]

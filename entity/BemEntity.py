from typing import List
from .GarantidorEntity import GarantidorEntity


class BemEntity:
    codigoBem: str
    garantidores: List[GarantidorEntity]

    def __repr__(self):
        return f"BemEntity(codigoBem='{self.codigoBem}', garantidores={self.garantidores})"

    def __dict__(self):
        return {
            'codigoBem': self.codigoBem,
            'garantidores': [garantidor.__dict__() for garantidor in self.garantidores]
        }
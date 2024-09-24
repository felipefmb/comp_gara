from typing import List
from .OperacaoEntity import OperacaoEntity
from .BemEntity import BemEntity


class GarantiaEntity:
    cod_gara: str
    operacoes: List[OperacaoEntity]
    bens: List[BemEntity]

    def __repr__(self):
        return f"GarantiaEntity(cod_gara='{self.cod_gara}', operacoes={self.operacoes}, bens={self.bens})"

    def __dict__(self):
        return {
            'cod_gara': self.cod_gara,
            'operacoes': [operacao.__dict__() for operacao in self.operacoes],
            'bens': [bem.__dict__() for bem in self.bens]
        }
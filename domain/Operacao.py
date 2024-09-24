from pydantic import BaseModel


class Operacao(BaseModel):
    codigoOperacao: str

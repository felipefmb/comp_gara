

class OperacaoEntity:
    codigoOperacao: str


    def __repr__(self):
        return f"OperacaoEntity(codigoOperacao='{self.codigoOperacao}')"

    def __dict__(self):
        return {'codigoOperacao': self.codigoOperacao}



class GarantidorEntity:
    codigoGarantidor: str


    def __repr__(self):
        return f"GarantidorEntity(codigoGarantidor='{self.codigoGarantidor}')"

    def __dict__(self):
        return {'codigoGarantidor': self.codigoGarantidor}
from comp_gara.domain.Garantia import Garantia
from comp_gara.domain.Garantidor import Garantidor
from comp_gara.domain.Operacao import Operacao
from comp_gara.entity.GarantiaEntity import GarantiaEntity
from comp_gara.entity.BemEntity import BemEntity
from comp_gara.domain.Bem import Bem
from comp_gara.entity.GarantidorEntity import GarantidorEntity
from comp_gara.entity.OperacaoEntity import OperacaoEntity
from util.util_json import carrega_json
from config import dynamodb

def to_bem_entity(bem: Bem) -> BemEntity:
    bem_entity: BemEntity  = BemEntity()
    bem_entity.codigoBem = bem.codigoBem
    bem_entity.garantidores = [to_garantidor_entity(garantidor) for garantidor in bem.garantidores]
    return bem_entity

def to_garantidor_entity(garantidor: Garantidor) -> GarantidorEntity:
    garantidor_entity: GarantidorEntity = GarantidorEntity()
    garantidor_entity.codigoGarantidor = garantidor.codigoGarantidor
    return garantidor_entity

def to_operacao_entity(operacao: Operacao) -> OperacaoEntity:
    operacao_entity: OperacaoEntity = OperacaoEntity()
    operacao_entity.codigoOperacao = operacao.codigoOperacao
    return operacao_entity

if __name__ == '__main__':
    evento = carrega_json('data')
    domain: Garantia = Garantia(**evento)
    entity: GarantiaEntity = GarantiaEntity()
    entity.cod_gara = domain.codigoGarantia
    entity.bens = [to_bem_entity(bem) for bem in domain.bens]
    entity.operacoes = [to_operacao_entity(operacao) for operacao in domain.operacoes]

    print("Domain: ", domain.__dict__)
    print("Entity: ", entity.__dict__)

    table_name = 'comp_gara'
    dynamodb.save(entity.__dict__(), table_name)


import json

def carrega_json(name_file: str):
    # Caminho do arquivo .json
    arquivo_json = f'./{name_file}.json'

    # Abrindo e carregando o conteúdo do arquivo para uma variável
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

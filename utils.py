import json

def load_data(notes):
    caminho = "static/data/" + notes
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados
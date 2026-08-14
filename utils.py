import json

def load_data(notes):
    caminho = "static/data/" + notes
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(index):
    with open( "static/templates/" + index, "r", encoding="utf-8") as f:
        return f.read()


def save_note(nova_anotacao):
    dados = load_data("notes.json")
    dados.append(nova_anotacao)

    with open("static/data/notes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
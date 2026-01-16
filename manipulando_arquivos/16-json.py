import json

dados = {
    "clientes":[
        {"id":1, "nome":"Ana", "idade":28, "cidade":"São Paulo"},
        {"id":2, "nome":"Bruno", "idade":34, "cidade":"Rio de Janeiro"},
        {"id":3, "nome":"Carla", "idade":25, "cidade":"Belo Horizonte"},
        {"id":4, "nome":"Daniel", "idade":30, "cidade":"Curitiba"}
    ]
}
caminho_arquivo = "dados/clientes.json"

#1- Escrevendo dados em um arquivo JSON
with open(caminho_arquivo, "w") as f:
    json.dump(dados, f, indent=4)

#2- Lendo dodos de um arquivo JSON
with open(caminho_arquivo, "r",encoding="utf-8") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)

#3- manipulando dados lidos
for client in dados_lidos["clientes"]:
    if client["nome"] == "Carla":
        client["idade"] = 20
        
novo_cliente = {"id":5, "nome":"Eduardo", "idade":29, "cidade":"Salvador"}
dados_lidos["clientes"].append(novo_cliente)

#4- Salvar dados maniipulados de volta no arquivo JSON
with open(caminho_arquivo, "w",encoding="utf-8") as f:
    json.dump(dados_lidos, f, indent=4)
    
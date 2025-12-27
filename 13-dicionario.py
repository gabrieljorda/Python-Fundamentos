filmeInception = {
    "titulo": "Inception",
    "year": 2010,
    "imdbRate": 8.8,
    "genres": ["Action", "Adventure", "Sci-Fi"],
}

print(filmeInception)
print(len(filmeInception))
print(type(filmeInception))

#1 - buscar elmento do dicionario
print(filmeInception["titulo"])
print(filmeInception.get("year"))
#2- bscar a chave do dicionario
print(filmeInception.keys())

#3 - buscar os valores do dicionario
print(filmeInception.values())

#4 - buscar itens de um dicionario com chave e valor
print(filmeInception.items())

#5 - adicionar novo item ao dicionario
filmeInception["director"] = "Christopher Nolan"
print(filmeInception)

#6 - atualizar valor de um item do dicionario
filmeInception.update({"imdbRate": 3.8})
print(filmeInception)

# 7 - remover item do dicionario
filmeInception.pop("year")
print(filmeInception)

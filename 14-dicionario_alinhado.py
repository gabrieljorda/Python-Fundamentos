import pprint
filmDict = {
    "Inception":{
    "year": 2010,
    "imdbRate": 8.8,
    "genres": ["Action", "Adventure", "Sci-Fi"],
    },
    "The Dark Knight":{
    "year": 2008,
    "imdbRate": 9.0,
    "genres": ["Action", "Crime", "Drama"],
    },
    "Interstellar":{
    "year": 2014,
    "imdbRate": 8.6,
    "genres": ["Adventure", "Drama", "Sci-Fi"],
    },
}
print(filmDict)
print(len(filmDict))
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmDict)


#1 buscar ma informação dentro de um dicionario ainhado
print(filmDict["Interstellar"]["genres"])

#2 Adicionar novo item
filmDict["Inception"]["director"] = "Cristopher Nolan"

#3 - Excluir um dicionario 
del filmDict["Inception"]
pp.pprint(filmDict)

# Escreva um programa que:

# Leia o nome de três produtos e seus respectivos preços.

# Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).

# Imprima:

# O dicionário completo.

# O produto mais caro.

# A média dos preços.

dic = {
    "Arroz":15.50,
    "Feijão":8.90,
    "Macarrão":6.75
}
print(dic)
print(max(dic, key=dic.get))
print(f"{sum(dic.values())/len(dic):.2f}")

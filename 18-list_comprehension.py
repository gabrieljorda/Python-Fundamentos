#listando valores de 0 a 10 que sejam menores do que 4 
listaNumeros = [i for i in range(10)]
print(listaNumeros)

#lista de filmes
filmes = [
    "O Poderoso Chefão",
    "O Senhor dos Anéis: O Retorno do Rei",
    "Parasita ",
    "Clube da Luta",
    "A Origem ",
    "Interestelar",
    "O Labirinto do Fauno",
    "Matrix",
    "Cidade de Deus",
    "Tudo em Todo Lugar ao Mesmo Tempo"
]

#filmes que possuem a letra 'o' no titulo

filmesName_o = [movie for movie in filmes if "o" in movie.lower]
print(filmesName_o)

#mapeando filmes que eu assisti 

moviesWatcher =[movie for movie in filmes if movie != "Tudo em Todo Lugar ao Mesmo Tempo"]
print(moviesWatcher)

#Encontrando filme pelo nome 
while True:
    serchName = input("digite o nome do filme para buscar na lista(oou sair para encerrar):\n")
    if serchName.lower()== "sair":
        break
    foundmovies = [movie for movie in filmes if serchName.lower() in movie.lower]
    if foundmovies:
        print(f"Filme(s) encontrado(s) com o nome:{serchName}")
        for foundmovies in foundmovies:
            print(foundmovies)
    else:
        print(f"Nenhum filme encontrado com nomme {serchName}.Tente novemente")
            
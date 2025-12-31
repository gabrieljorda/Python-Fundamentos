# Lista de filmes
filmes = [
    "O Poderoso Chefão (1972)",
    "O Senhor dos Anéis: O Retorno do Rei (2003)",
    "Parasita (2019)",
    "Clube da Luta (1999)",
    "A Origem (2010)",
    "Interestelar (2014)",
    "O Labirinto do Fauno (2006)",
    "Matrix (1999)",
    "Cidade de Deus (2002)",
    "Tudo em Todo Lugar ao Mesmo Tempo (2022)"
]

print(filmes)
# interando valores da lista
for movie in filmes:
    print(movie)

#Qaundo a condição for atendida o loop será encerrado
for movie in filmes:
    if movie == "Matrix (1999)":
        break
    print(movie)

#quando a condeção for atendida,  o loop vai para a proxima interação
for movie in filmes:
    if movie == "Matrix (1999)":
        continue
    print(movie) 

#Avaliação do filme
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0 
for i in range(movieRating):
    note = float(input("digite a nota para o filme:\n"))
    total += note

if movieRating > 0 :
    average = total / movieRating
else:
    average = 0
    
print(f"Media de avaliação do filme {movieName} é: {average:.2f}")
    
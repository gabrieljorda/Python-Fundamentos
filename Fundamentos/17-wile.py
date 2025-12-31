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

# interando valories de uma lista de filmees usando while
index = 0
while index < len(filmes):
    print(filmes[index])
    index += 1
    
#Quando a condição for atendida o loop será encerrado

index = 0
while index < len(filmes):
    if filmes[index] == "Interestelar (2014)":
        index +=1
        continue
    print(filmes[index])
    index += 1
    
#quando a condição for atendida o loop vai para a proxima interação
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("digite a nota para o filme:\n"))
    total += note
    count +=1
    
if movieRating > 0 :
    average = total / movieRating
else:
    average = 0
    
print(f"Media de avaliação do filme {movieName} é: {average:.2f}")
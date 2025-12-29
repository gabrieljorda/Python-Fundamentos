#função para imprimir uma mensagem
def welcome():
    print("bem vindo ao sistema de Filmes!")


welcome()

#função para calcular a media de notas

def calcular_avarage():
    num_ratings = int(input("Digite quantas avaliações quer fazer sobre o filme: \n"))

    total = 0 
    for i in range(num_ratings):
        note = float(input("digite a nota para o filme:\n"))
        total += note
    if num_ratings >0 :
        average = total / num_ratings
    else:
        average = 0
        
    return average

print(f"A media das avaliações é:{calcular_avarage():.2f}")

#dunção para cadastrar um filme 

def create_movie():
    nome = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digite o ano do Lançamento:\n"))
    moviePrice = float(input("Digite o preço do filme "))
    noteMovie = float(input("Digite a:\n"))
    
    
    print(f"{nome} ({yearLaunch}) - R$ {moviePrice:.2f} ")

create_movie()
create_movie()
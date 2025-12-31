#funçao para imprimir um nome completo 
def full_name(first_name,last_name):
    print(f"Nome é:{first_name} {last_name}\n")
    
full_name("Fulano","Siclano")
full_name("João", "Costa")

#função para somar 2 numeros
def sum_numbers(a,b):
    return a+b

print(f"Soma é:{sum_numbers(15,20)}")


# função com parametro default

def address(country="Brasil"):
    print(f"Eu moro em :{country}")

address("Portugal")

def rete_movie(num_ratings,movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total+=note
    if num_ratings >0 :
        average = total / num_ratings
    else:
        average = 0
        
    print(f"Média de avaliação do filme : {movie_name} é : {average:.2f}")

rete_movie(2 , "Sonic")


#Função de potencia de um número
power = lambda num: num **2

#função que verifica o número é paar
is_even = lambda x: x % 2 == 0

# Função que divide um número por outro
div_num = lambda x , y:  x / y

#Função que inverte uma palavra 
reverse_string = lambda s: s[::-1]



print(power(5))
print(power(9))
print(is_even(27))
print(is_even(18))
print(div_num(10,2))
print(div_num(6,2))
print(reverse_string("Python"))
print(reverse_string("Javascript"))

#Funcionalidades relacionada aos filmes:
movies_list = ["Titanic","The GodFather","Inception","Jurassic Park","The Matrix"]
ratings = {
    "Titanic":[8.5,9.0,10],
    "The GodFather":[4.0,5.0,8.0],
    "Inception":[8.1,9.2,8.6],
    "Jurassic Park":[4.0,5.0,8.0],
    "The Matrix":[8.5,9.0,10]    
}

#Função para calcular a média de avaliações de um filme 
average_rating = lambda movies_name :sum(ratings[movies_name]) / len(ratings[movies_name])

#função que verifica se um filme está na lista 
check_movie = lambda movie_name: movie_name in movies_list

#Função pra recomendar um filme com base na avaliação  média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"

print(f"Media de avaliações do filme The Matrix:{average_rating("The Matrix")}")
print(f"O filme Titanic está na lista? {check_movie("Titanic")}")
print(recommend_movie("Titanic"))
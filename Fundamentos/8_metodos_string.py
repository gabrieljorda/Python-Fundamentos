moveName = "Mario Kart"
movieDescription = "Um jogo de corrida com personagens da Nintendo."

print(moveName.upper())  # Deixa todas as letras maiúsculas
print(moveName.lower())  # Deixa todas as letras minúsculas
print(moveName.capitalize())  # Deixa a primeira letra maiúscula
print(moveName.title())  # Deixa a primeira letra de cada palavra maiúscula
print(moveName.center(10 , '-'))  # Centraliza a string em um campo de 30 caracteres
print(moveName.find("K"))  # Retorna o índice da primeira ocorrência da substring
print(moveName.find("z"))  # Retorna -1 se a substring não for encontrada
print(moveName.replace("Mario", "Luigi"))  # Substitui uma substring por outra
print(moveName.split(" "))  # Divide a string em uma lista com base no separador

# Escreva um programa que leia uma palavra e um número inteiro n.
# O programa deve:

# Imprimir a palavra duas vezes concatenada (sem espaço).

# Imprimir a palavra repetida n vezes (usando multiplicação de string).

word = input("Digite uma palavra: ")
n = int(input("Digite um número inteiro: "))
print(word + word)
print(word * n)
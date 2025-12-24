filmesList = ["Matrix", "Vingadores Ultimato","O poderoso chefão",]

#1-tamanho da lista
print(len(filmesList))

#2-recuperar um intem da lista pelo indice
print(filmesList.index("O poderoso chefão"))

#3 - adicionando um item na lista
filmesList.append("Interestelar")
print(filmesList)
#4 - ordenando lista
filmesList.sort() 
print(filmesList)

#5- Copiando itens de uma lista para outra
novosFilmes = filmesList.copy()
print(novosFilmes)
novosFilmes.remove("Matrix")
print(novosFilmes)

#6 - Removendo todos os item da lista
filmesList.clear()
print(filmesList)


# Escreva um programa que:

# Leia 3 números inteiros.

# Armazene esses números em uma lista.

# Imprima:

# A lista completa.

# O primeiro elemento da lista.

# A soma de todos os elementos da lista.

numeros = []
for i in range(3):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
print( numeros)
print( numeros[0])
print(sum(numeros))
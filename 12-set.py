filmeSet = {"O Poderoso Chefão", "Forrest Gump", "A Origem", "Clube da Luta"}

print(type(filmeSet))

#1 - Buscar a quantidade de itens no set

print(len(filmeSet))

#2 - O valor True e 1 sao considerados o mesmo valor 

numerosSet = {1, 2, 3, 4, 5, True}
print(len(numerosSet))

#3 - adicionar item de outro set
outroSet = {"Interestelar", "Matrix"}
filmeSet.update(outroSet)
print(filmeSet)

#4 - remover item do set
filmeSet.remove("Forrest Gump")
print(filmeSet)

# Escreva um programa que:

# Leia cinco números inteiros (podendo haver repetidos).

# Armazene-os em um set para eliminar duplicatas.

# Imprima:

# O set resultante.

# A quantidade de elementos únicos.

# O maior elemento do set.

lista1  = []
while len(lista1) < 5:
    numero = int(input("Digite um número inteiro: "))
    lista1.append(numero)
numerosSet = set(lista1)
print(numerosSet)
print(len(numerosSet))
print(max(numerosSet))


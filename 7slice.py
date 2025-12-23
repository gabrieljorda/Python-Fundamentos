movieName = "o poderoso chefão"

#string[inicio:fim] - indice começa na posição 0 \ indice final -1

#1 - buscar toda a string a partir da primeira posição
print(movieName[0:])

#2 -buscar toda string ate a ultima posição
print(movieName[:len(movieName)])

# - Buscando toda string a partir da posição 3 até a ultima posição
print(movieName[3:])

"""#string[inicio:fim:passo] 
indice começa na posição 0 \ indice final -1
passo - determina o incremento. por padrao é 1
"""

#4 - buscar toda a string de 2 emm 2 caracteres
print(movieName[::2])

# 5 - buscar toda a string nos indices inpares
print(movieName[1::2])

#6 - buscar a string de tras para frente
print(movieName[::-1])
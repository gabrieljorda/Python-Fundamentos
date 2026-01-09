"""
Arquivos - Modos de Operação

1 - Modo W - write
2 - Modo A - append
3 - Modo R - read
"""

with open("manipulando_arquivos/dados/names.txt" , "r" , encoding="utf-8") as file:
    # print(file.read())
    for line in file:
        print(f"Olá , {line.strip()}")



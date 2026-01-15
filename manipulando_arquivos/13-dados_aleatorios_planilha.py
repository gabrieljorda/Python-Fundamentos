import pandas as pd
import numpy

dados_aba1 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["João", "Maria", "Pedro", "Ana", "Lucas"],
    "Idade": [25, 30, 35, 40, 45],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Porto Alegre"]
}

dados_aba2 = {
    "ID": [6, 7, 8, 9, 10],
    "Nome": ["Mariana", "Lucas", "Ana", "Pedro", "João"],
    "Idade": [20, 25, 30, 35, 40],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Porto Alegre"]
}

dados_aba3 = {
    "ID": [11, 12, 13, 14, 15],
    "Nome": ["João", "Maria", "Pedro", "Ana", "Lucas"],
    "Idade": [45, 50, 55, 60, 65],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Porto Alegre"]
}

dados_aba4 = {
    "ID": [16, 17, 18, 19, 20],
    "Nome": ["Mariana", "Lucas", "Ana", "Pedro", "João"],
    "Idade": [30, 35, 40, 45, 50],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Porto Alegre"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)

caminh_arquivo = "dados/clientes.xlsx"

with pd.ExcelWriter(caminh_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba1", index=False)
    df_aba2.to_excel(writer, sheet_name="Aba2", index=False)
    df_aba3.to_excel(writer, sheet_name="Aba3", index=False)
    df_aba4.to_excel(writer, sheet_name="Aba4", index=False)

print(f"Arquivos exel com 4 abas criados em {caminh_arquivo}")

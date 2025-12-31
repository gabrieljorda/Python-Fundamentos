"""
*args - Utilizamos ele quando não temos certeza quantos argumentos queremos ter numa função.
- Os argumentos são passados como uma tupla
**kwargs -Além dos valores podemos passar também as respectivas chaves para cada argumrnto.
- Os argumentos são passados como dicionario
"""
# somando numeros 
def sum(*num):
    sum_total = 0 
    for n in num :
        sum_total += n 
    print(f"Soma é:{sum_total}")

sum(7)
sum(7,9)
sum(7,5,6,3,4)

def presentation(**data):
    for key , value in dara.items():
        print(f"{key} - {value}")

print("liesta de Cursos:")
presentation(nome="Python", category = "Backend" , level ="Iniciante")
presentation(nome="Visão Computacional com Python", category = "IA" , level ="Avançado")
presentation(nome="Dashboards com Dash", category = "Data Science" , level ="Intermediário")

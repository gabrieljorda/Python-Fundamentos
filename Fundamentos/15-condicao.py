# Informaçoes sobre o filme
name = input("Digite o nome do filme:\n")
yearRelese = int(input("Digite o ano de lançamento:\n"))
rating = float(input("Digite a nota de avaliação do filme:\n"))

#Verifica se o filme é recomendado
if rating > 8.0 and yearRelese > 2015:
    print(f"O filme {name} é muito bom. Recomendo assisti-lo. ")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota.")
    

num1 = float(input("digite o primeiro numero:\n"))
num2 = float(input("digite o segundo numero:\n"))
operador = input("Digite a operação a ser realizada:(+ - * /)\n")

if operador == "+":
    result = num1 +num2
    print(f"O resultado é:{result}")
elif operador == "-":
    result = num1 - num2
elif operador == "*":
    result = num1 * num2
elif operador == "/":
    if num2 != 0 :
        result = num1 / num2
        print(f"O resultado é:{result}")
    else:
        print("Erro: divisão por Zero")
        result = 0
else:
    print("Operação invalida")
    result = 0
    
print(f"O resultado da operação é:{result:.2f}")

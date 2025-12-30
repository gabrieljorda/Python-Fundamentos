"""
fatorial de um número 
1-> 1 * 1  = 1 
2->  2 * 1 = 2
3-> 3 * fatorial(2) = 6
"""
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num -1))

number = int(input("Digite o número para o fatorial:\n"))
print(f"O fatorial de {number} é {factorial(number)} ")

# soma total de um numero 

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num -1))

num = int(input("Digite o número para a soma:\n"))
print(f"O soma total de {num} é {total_sum(num)} ")
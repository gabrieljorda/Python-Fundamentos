# Decorator
# - Modificam ou estemdem o comportamento de funções existentes de forma reutilizáveis.
# - Adicionam funcionalidades a funções existentes sem modificar seu código diretamente  .

from decorator import my_decorator, uppercase_decorator , split_string

@my_decorator  
def my_function():
    print("dentro da função")

my_function()

@split_string
@uppercase_decorator
def text():
    return "Hello World"

print(text())

@split_string
@uppercase_decorator
def exemple():
    return "Aprendendo Python e crindo decorators"
    
print(exemple())
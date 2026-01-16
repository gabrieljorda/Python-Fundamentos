import pickle

class Client:
    def __init__(self, name, idade , cidade):
        self.name = name
        self.idade= idade
        self.cidade = cidade
        
    def __str__(self):
        return f"{self.name}, {self.idade} anos, {self.cidade}"

    
cliente = [
    Client("Ana", 28, "São Paulo"),
    Client("Bruno", 35, "Rio de Janeiro"),
    Client("Carla", 22, "Belo Horizonte")
]
#Salvar lista de cliente em um arquivo pickle
with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(cliente, f)

#carregando dados do arquivo pickle
with open("dados/clientes.pkl", "rb") as f:
    clientes_carregados = pickle.load(f)
    
for c in clientes_carregados:
    print(c)

    
# Adicionando um novo cliente ao arquivo pickle existente
novo_cliente = Client("Daniel", 30, "Curitiba")
clientes_carregados.append(novo_cliente)

with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(clientes_carregados, f)
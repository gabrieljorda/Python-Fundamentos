import os

def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("informe o telefone\n")
    
    contact = f"Nome: {name} \nEndereço: {address} \nTelefone: {phone}\n"

    with open("manipulando_arquivos/dados/contatos.txt", "a" , encoding="utf-8") as file :
        file.write(contact)

def view_contacts():
    if not os.path.exists("manipulando_arquivos/dados/contatos.txt"):
        print("A lista de contatos está vazia")
        return ""
    with open("manipulando_arquivos/dados/contatos.txt", "r",encoding="utf-8") as file:
        contacts = file.read()
    print("lista de contatos:")
    print(contacts)

def delete_contacts():
    if not os.path.exists("manipulando_arquivos/dados/contatos.txt"):
        print("A lista de contatos está vazia")
        return ""
    with open("manipulando_arquivos/dados/contatos.txt", "w",encoding="utf-8") as file:
        file.write("")

    print("Contatos excluidos com sucesso")


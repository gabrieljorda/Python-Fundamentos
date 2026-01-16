import xml.etree.ElementTree as ET

dados = """<?xml version='1.0' encoding='UTF-8'?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Ana</nome>
        <idade>28</idade>
        <cidade>São Paulo</cidade>
    </cliente>
    <cliente>
        <id>2</id>
        <nome>Bruno</nome>
        <idade>35</idade>
        <cidade>Rio de Janeiro</cidade>
    </cliente>
</clientes>
"""

caminho_arquivo = 'dados/clientes.xml'

#Exportando dados para um arquivo XML
with open(caminho_arquivo, 'w', encoding='utf-8') as f:
    f.write(dados)

# lendo dados do arquivo xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

for cliente in root.findall('cliente'):
    id_cliente = cliente.find('id').text
    nome = cliente.find('nome').text
    idade = cliente.find('idade').text
    cidade = cliente.find('cidade').text
    print(f"ID: {id_cliente}, Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
    
# Adicionando um novo cliente
novo_cliente = ET.Element('cliente')
id_novo = ET.SubElement(novo_cliente, 'id')
id_novo.text = '3'
nome_novo = ET.SubElement(novo_cliente, 'nome')
nome_novo.text = 'Carlos'
idade_novo = ET.SubElement(novo_cliente, 'idade')
idade_novo.text = '30'
cidade_novo = ET.SubElement(novo_cliente, 'cidade')
cidade_novo.text = 'Belo Horizonte'

root.append(novo_cliente)

#Salvando no XML

tree.write(caminho_arquivo, encoding='utf-8', xml_declaration=True)
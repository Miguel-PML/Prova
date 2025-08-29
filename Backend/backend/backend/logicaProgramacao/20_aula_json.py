import json

inventario = []

try:
    with open('loja.json','r') as arquivo:
        inventario = json.load(arquivo)
        print("Arquivo carregado!")

except FileNotFoundError:
    print("Arquivo não encontrado")

print("/n-----CADASTRAR PRODUTO-----")

nome_produto = input("Digite o nome do produto: ")

while True:
    try:
        quantidade = int(input("Digite a quantidade: "))
        break
    
    except ValueError:
        print("Digite apenas números")

while True:
    try:
        preco = float(input("Digite o preço: "))
        break

    except ValueError:
        print("Digite o preço corretamente")

novo_produto = {
    "Nome_produto": nome_produto,
    "Quantidade": quantidade,
    "Preco": preco,
    "Tem_estoque": quantidade > 0 
}

#Escrever no arquivo json

inventario.append(novo_produto)
with open('loja.json','w') as arquivo:
    json.dump(inventario,arquivo,indent=4)

print(f"/n O produto {nome_produto} foi cadastrado")
def gerar_lista_compras():
    print("Seja bem-vindo, vamos as compras")
    print("Ao encerrar digite fim")

    with open("comida.txt", 'w') as comida:
        while True:
            item = input("Digite o item: ")
            if item.lower()=="fim":
                print("Encerrando lista")
                break
            comida.write(item + "\n")

gerar_lista_compras()

def listar_itens():
    with open("comida.txt", 'r') as lista:
        print("----Lista de compras----")
        for item in lista:
            produto = item.strip()
            print("item: ", produto)

listar_itens()
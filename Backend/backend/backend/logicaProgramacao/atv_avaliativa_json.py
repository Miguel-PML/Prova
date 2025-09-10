import json
armazem_categoria = []
armazem_produto = []

id_categoria = 0
id_produto = 0

def menu():
    print("1)Cadadastrar categoria")
    print("2)Cadastrar produto")
    print("3)Listar produtos")
    print("4)Sair")

def cadastrar_categoria():
    global id_categoria
    print("\nCadastro categoria:")
    nome_categoria = input("Nome: ")
    id_categoria +=1

    categoria = {
        "id_categoria" : id_categoria,
        "nome_categoria" : nome_categoria
    }

    armazem_categoria.append(categoria)
    print(" Categoria salva ")


def cadastrar_produto():
    global id_produto

    if not armazem_categoria:
        print("Erro: Nenhuma categoria cadastrada. Cadastre uma categoria primeiro.")
        return
    
    for cat in armazem_categoria:
        print(f"  ID: {cat['id_categoria']} - Nome: {cat['nome_categoria']}")

    id_produto += 1
    nome_produto = input("Nome: ")
    preco = int(input("Preço: "))
    id_categoria_associado = int(input("ID_Categoria: "))

    produto = {
        "id_produto" : id_produto,
        "nome_produto" : nome_produto,
        "preco" : preco,
        "id_categoria_associado" : id_categoria_associado
    }

    armazem_produto.append(produto)
    print(" Produto salvo ")


def listar_produtos():
    if not armazem_produto and armazem_categoria:
        print("\n Nenhum produto cadastrado.")
        return
    



while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_produto()
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        print("Encerrando sistema. Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.")
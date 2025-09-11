import json

armazem_categoria = []
armazem_produto = []

id_categoria = 0
id_produto = 0

e_commerce = 'e_commerce.json'

def salvar_dados():
    dados = {
        "categorias": armazem_categoria,
        "produtos": armazem_produto
    }
    with open(e_commerce, 'w') as f:

        json.dump(dados, f, indent=4)
    print("Dados salvos")

def carregar_dados():
    global armazem_categoria, armazem_produto, id_categoria, id_produto

    try:
        with open(e_commerce, 'r') as f:
            dados_carregados = json.load(f)
            armazem_categoria = dados_carregados.get("categorias", [])
            armazem_produto = dados_carregados.get("produtos", [])
            
            print("Dados carregados")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    except (json.JSONDecodeError, KeyError):
        print("Erro ao ler o arquivo de dados.")


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
    if not armazem_produto:
        print("Nenhum produto cadastrado.")
        return

    for produto in armazem_produto:
        nome_categoria_encontrado = "Categoria não encontrada"
        
        for categoria in armazem_categoria:
            if categoria["id_categoria"] == produto["id_categoria_associado"]:
                nome_categoria_encontrado = categoria["nome_categoria"]
                break 

        print(f"ID do Produto: {produto['id_produto']}")
        print(f"  Nome: {produto['nome_produto']}")
        print(f"  Preço: R$ {produto['preco']}") 
        print(f"  Categoria: {nome_categoria_encontrado}")

carregar_dados()


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
        salvar_dados()
        print("\nEncerrando sistema. Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.")

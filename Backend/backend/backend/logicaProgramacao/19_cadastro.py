ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios():

    try:
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
            usuarios = [linha.strip() for linha in arquivo]
            return usuarios
    except FileNotFoundError:

        return []

def salvar_usuarios(lista_usuarios):
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
        for usuario in lista_usuarios:

            arquivo.write(f"{usuario}\n")

def cadastro_usuario():
    
    escolha = 0

    usuarios = carregar_usuarios()

    while escolha != 5:

        print("\n--- MENU ---")
        print("1) Cadastrar Usuário")
        print("2) Verificar cadastro")
        print("3) Alterar Nome de Usuário")
        print("4) Excluir Usuário")
        print("5) Sair")

        try:
            escolha = int(input("Digite o número do que quer fazer: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número.")
            continue

        match escolha:

            case 1:
                print("\n------ Cadastro de Usuário ------")
                print("Digite os nomes. Quando terminar, digite FIM.")

                while True:
                    nome_usuario = input("Nome de Usuário: ").strip().lower()
                    if nome_usuario == "fim":
                        break
                    
                    usuarios.append(nome_usuario)
                    salvar_usuarios(usuarios) 
                    print(f"Usuário '{nome_usuario}' cadastrado e salvo com sucesso!")

            case 2:
                print("\n--- Verificação ---")
                verificacao_usuario = input("Nome do Usuário a verificar: ").strip().lower()
                
                if verificacao_usuario in usuarios:
                    print(f"Sim, o usuário '{verificacao_usuario}' está cadastrado.")
                else:
                    print(f"Não, o usuário '{verificacao_usuario}' não está cadastrado.")

            case 3:
                print("\n--- Alteração de Usuário ---")
                usuario_antigo = input("Digite o nome do usuário que deseja alterar: ").strip().lower()

                if usuario_antigo in usuarios:
                    novo_nome = input(f"Digite o novo nome para '{usuario_antigo}': ").strip().lower()
                    indice = usuarios.index(usuario_antigo)
                    usuarios[indice] = novo_nome
                    salvar_usuarios(usuarios) 
                    print("Usuário alterado e salvo com sucesso!")
                else:
                    print(f"Usuário '{usuario_antigo}' não encontrado!")

            case 4:
                print("\n--- Excluir Usuário ---")
                usuario_a_excluir = input("Digite o nome do usuário que deseja excluir: ").strip().lower()

                if usuario_a_excluir in usuarios:
                    usuarios.remove(usuario_a_excluir)
                    salvar_usuarios(usuarios)
                    print(f"Usuário '{usuario_a_excluir}' excluído e salvo com sucesso!")
                else:
                    print(f"Usuário '{usuario_a_excluir}' não encontrado!")
            
            case 5:
                print("\nSaindo do programa. Até logo!")
            
            case _:
                print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")

cadastro_usuario()
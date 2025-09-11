
#eu como um dono de concessionária de carros importados, preciso de um sistema para controlar meu estoque de veículos.
#para me organizar melhor, além do nome gostaria de guardar o ano, quilometragem, marca, preço, cor e quantidade de cada veículo.
#quero um menu, onde eu possa cadastrar, alterar, excluir e listar meus veículos.
#para me sentir especial, quero que o nome da minha loja apareça no topo do menu

#Nome da loja: Moya’s imports


# Nossa lista que funciona como banco de dados.
estoque = []

def mostrar_menu():
    """Imprime o menu principal da loja."""
    print("        ----Moya’s imports----")
    print("----Sistema de Controle de Estoque----")
    print("1. Cadastrar Veículo")
    print("2. Listar Veículos")
    print("3. Alterar Veículo")
    print("4. Excluir Veículo")
    print("5. Sair")


def listar_veiculos():
    """Exibe todos os veículos cadastrados no estoque."""
    print("\n--- Lista de Veículos em Estoque ---")
    if not estoque:
        print("Nenhum veículo cadastrado no momento.")
        return False # Retorna False para indicar que a lista está vazia

    for i, v in enumerate(estoque):
        print(f"\nID: {i} | {v['marca']} {v['nome']} ({v['ano']})")
        print(f"  Cor: {v['cor']} | KM: {v['km']} | Preço: R$ {v['preco']:.2f} | Qtd: {v['quantidade']}")
    return True # Retorna True para indicar que há veículos na lista

def cadastrar_veiculo():
    """Pede os dados de um veículo e o adiciona ao estoque."""
    print("\n--- Cadastro de Novo Veículo ---")
    try:
        veiculo = {
            'nome': input("Nome do veículo: "),
            'marca': input("Marca: "),
            'cor': input("Cor: "),
            'ano': int(input("Ano: ")),
            'km': int(input("Quilometragem: ")),
            'preco': float(input("Preço: ")),
            'quantidade': int(input("Quantidade: "))
        }
        estoque.append(veiculo)
        print(f"\n[SUCESSO] Veículo '{veiculo['marca']} {veiculo['nome']}' cadastrado!")
    except ValueError:
        print("\n[ERRO] Dados inválidos. Ano, KM, preço e quantidade devem ser números.")

def _selecionar_veiculo():
    """Função auxiliar para listar e selecionar um veículo pelo ID."""
    if not listar_veiculos(): # Se a lista estiver vazia, não continua
        return None
    
    try:
        id_selecionado = int(input("\nDigite o ID do veículo: "))
        if 0 <= id_selecionado < len(estoque):
            return id_selecionado # Retorna o índice do veículo na lista
        else:
            print("\n[ERRO] ID inválido.")
            return None
    except ValueError:
        print("\n[ERRO] ID deve ser um número.")
        return None

def alterar_veiculo():
    """Altera os dados de um veículo selecionado."""
    id_para_alterar = _selecionar_veiculo()
    
    if id_para_alterar is not None:
        print("\n--- Insira os novos dados para o veículo ---")
        try:
            veiculo_alterado = {
                'nome': input("Novo nome: "),
                'marca': input("Nova marca: "),
                'cor': input("Nova cor: "),
                'ano': int(input("Novo ano: ")),
                'km': int(input("Nova quilometragem: ")),
                'preco': float(input("Novo preço: ")),
                'quantidade': int(input("Nova quantidade: "))
            }
            estoque[id_para_alterar] = veiculo_alterado
            print("\n[SUCESSO] Veículo alterado com sucesso!")
        except ValueError:
            print("\n[ERRO] Dados inválidos. A alteração foi cancelada.")

def excluir_veiculo():
    """Exclui um veículo do estoque."""
    id_para_excluir = _selecionar_veiculo()

    if id_para_excluir is not None:
        veiculo_removido = estoque.pop(id_para_excluir)
        print(f"\n[SUCESSO] Veículo '{veiculo_removido['marca']} {veiculo_removido['nome']}' foi excluído.")

# --- Programa Principal ---
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_veiculo()
    elif opcao == '2':
        listar_veiculos()
    elif opcao == '3':
        alterar_veiculo()
    elif opcao == '4':
        excluir_veiculo()
    elif opcao == '5':
        print("\nObrigado por usar o sistema da Moya's imports. Até logo!")
        break
    else:
        print("\n[ERRO] Opção inválida. Tente novamente.")
    
    input("\nPressione Enter para continuar...")
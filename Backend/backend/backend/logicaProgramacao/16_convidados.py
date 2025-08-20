def lista_de_convidados():
   
    convidados = []
    print("--- Cadastro de Convidados ---")
    print("Digite o nome de cada convidado. Digite 'fim' para encerrar o cadastro.")

    while True:
        nome_convidado = input("Nome do convidado: ").strip().lower()
        if nome_convidado == 'fim':
            break
        convidados.append(nome_convidado)

    print("\n--- Verificação de Entrada ---")
    while True:
        nome_verificacao = input("Digite seu nome (ou 'sair' para encerrar): ").strip().lower()
        if nome_verificacao == 'sair':
            break
        
        if nome_verificacao in convidados:
            print("Pode entrar. Bem-vindo(a)!")
        else:
            print("Entrada negada. Você não está na lista de convidados.")

if __name__ == "__main__":
    lista_de_convidados()
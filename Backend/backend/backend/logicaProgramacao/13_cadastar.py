cadastro = input("Digite seu nome para o cadastro: ")
saldo = 0 
escolha = ""

while escolha != "sair" and escolha != "Sair":
    
    print("Qual seu objetivo?")

    print("1) Sacar ")
    print("2) Depositar ")
    print("3) Saldo ")
    print("4) Sair ")

    escolha = input("Digite o que deseja fazer: ")

    match escolha:
        case "Depositar"|"depositar"|"2":
            deposito = float(input("Qual o valor que deseja depositar?: R$ "))
            saldo = saldo + deposito

        case "Sacar"|"sacar"|"1":
            sacar = float(input("Qual o valor da retirada?: R$ "))
            if (sacar <= saldo):
                saldo = saldo - sacar
                print("Seu saque foi bem sucedido")

            else:
                print("Saldo insuficiente")

        case "Saldo"|"saldo"|"3":
            print(f"Olá {cadastro}. Seu saldo é de R$ ",saldo)

        case "Sair"|"sair":
            print("Tchau")


        case _:
            print("Erro")

print("Foi um prazer, até logo :)")
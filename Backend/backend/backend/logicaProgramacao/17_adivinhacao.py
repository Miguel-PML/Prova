def jogo_da_palavra():
   
    palavra = []

    print("Digite a palavra secreta.")

    while True:
        secreto = input("palavra secreta : ").strip().lower()
        break
    palavra.append(secreto)

    print("\n--- Verificação ---")
    while True:
        palavra_verificacao = input("Digite a palavra escreta (ou 'sair' para encerrar): ").strip().lower()
        if palavra_verificacao == 'sair':
            break
        
        if palavra_verificacao in palavra:
            print("parabéns")
            break
        else:
            print("tente novamente")

if __name__ == "__main__":
    jogo_da_palavra()

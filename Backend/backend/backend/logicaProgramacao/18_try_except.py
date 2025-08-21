#*:
    #try:
        # Bloco de código onde um erro pode ocorrer
        # (Plano A)
        
    #except TipoDeExcecao:
        # Bloco de código que será executado SE algum erro ocorrer no Try
        # (Plano B)

    #try:
        # Tente executar este código.

    #except TipoDeExcecao1 as e:
        # Execute este bloco se 'TipoDeExcecao1' ocorrer.

    #except (TipoDeExcecao2, TipoDeExcecao3) as e:
        # Execute este bloco se 'TipoDeExcecao2' ou 'TipoDeExcecao3' ocorrerem.

    #else:
        # Execute este bloco se NENHUMA exceção ocorreu no 'try'.

    #finally:
        # Execute este bloco SEMPRE, independentemente do que aconteceu.


lista_de_convidados = []
nome_arquivo = "convidados.txt"

print("--- CADASTRO DE CONVIDADOS ---")
print("Digite o nome de cada convidado. Ao terminar, digite 'FIM'.")

while True:
   
    nome = input("Digite o nome do convidado: ")

   
    if nome.upper() == 'FIM':
        break  
    else:
       
        lista_de_convidados.append(nome)
        print(f"'{nome}' foi adicionado à lista.")

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    for convidado in lista_de_convidados:
       
        arquivo.write(convidado + '\n')

print("\nCadastro finalizado! A lista de convidados foi salva em '{}'.".format(nome_arquivo))
print("-" * 30)


# --- PARTE 2: VERIFICAÇÃO DE ENTRADA ---

print("\n--- VERIFICAÇÃO DE ENTRADA ---")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        
        convidados_do_arquivo = [linha.strip() for linha in arquivo.readlines()]

    nome_para_verificar = input("Digite o nome para verificar na lista: ")

    if nome_para_verificar in convidados_do_arquivo:
        print("\nResultado: PODE ENTRAR")
    else:
        print("\nResultado: ENTRADA NEGADA")

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado. Execute a parte de cadastro primeiro.")

#-------------------------------------------------------------------------------------------------------------------

def adicionar_log(mensagem, nome_arquivo="eventos.log"):
    """Adiciona uma mensagem (convertida para string) a um arquivo de log."""
    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(str(mensagem) + '\n')
    except IOError as e:
        # Apenas imprime o erro, não precisa parar a execução
        print(f"Erro ao escrever no log '{nome_arquivo}': {e}")

def ler_arquivo(caminho_arquivo):
    """Lê um arquivo e retorna seu conteúdo, ou None em caso de erro."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    # PONTO 1: Capturando exceções mais específicas.
    except (FileNotFoundError, IOError, UnicodeDecodeError) as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None

# PONTO 2: Bloco principal para organizar a execução do script.
if __name__ == "__main__":
    
    # Define o nome do arquivo uma vez para evitar repetição
    nome_do_log = "eventos.log"

    # 1. Fase de Escrita: gravamos todos os logs.
    print("--- Gravando logs ---")
    adicionar_log("Servidor iniciado.")
    adicionar_log("Conexão recebida do IP 192.168.1.100.")
    adicionar_log(f"Código de status: {200}") 
    adicionar_log({"erro": "timeout", "tentativa": 3})
    print("Gravação de logs finalizada.")

    # 2. Fase de Leitura: lemos o arquivo gerado e mostramos o resultado.
    print("\n--- Conteúdo do log ---")
    conteudo_do_log = ler_arquivo(nome_do_log)
    
    # Verifica se a leitura foi bem-sucedida antes de imprimir
    if conteudo_do_log:
        print(conteudo_do_log)
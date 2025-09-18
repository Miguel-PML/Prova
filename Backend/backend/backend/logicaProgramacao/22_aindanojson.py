import json

def cadastrar_livro():
    """
    cadastrar e livros na biblioteca
    """
    print("---Cadastrar Livro---")
    titulo = input("Digite o titulo: ")
    autor = input("Digite o nome do autor: ")

    while True:
        try:
            numero_paginas= int(input("Digite o número de paginas: "))
            break
        
        except ValueError:
            print("Resposta invalida. Digite um número")
            
    editora = input("Digite o nome da editora: ")
    genero = input("Digite o genero do livro: ")
    idioma = input("Digite o idioma do livro: ")

    while True:
        try:
            ano_publicacao = int(input("Digite o ano que foi publicado: "))
            break
        
        except ValueError:
            print("Resposta invalida. Digite um número")

    return {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "ano_publicacao": ano_publicacao,
        "genero": genero,
        "numero_paginas": numero_paginas,
        "idioma": idioma
    }

def main():
    """
    Gerencia o cadastro, salvamento dos dados e a leitura
    """
    nome_arquivo = "biblioteca.json"
    livro = []
    
    try:
        with open(nome_arquivo, "r") as arquivo:
            livro = json.load(arquivo)
        print(f"Dados existentes carregados com sucesso do arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando um novo cadastro.")
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo '{nome_arquivo}'. O arquivo pode estar corrompido. Iniciando um novo cadastro.")

    # Laço principal para o cadastro
    while True:
        novo_livro = cadastrar_livro()
        livro.append(novo_livro)
        
        continuar = input("\nDeseja cadastrar outro livro? (s/n): ").lower()
        if continuar != 's':
            break

    # Salvar a lista atualizada no arquivo
    try:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(livro, arquivo, indent=4)
        print(f"\nTodos os livros foram salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"\nOcorreu um erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()

    """
with open(nome_arquivo, "r") as arquivo:
            produto_para_auterar = int(input("Digite o ID do produto: "))
            livro = json.load(arquivo)
            for nome_livro in livro:
                if produto_para_auterar == nome_livro["id"]:
                    novo_nome = input("Digite o novo nome")
                    nome_livro["nome"] = novo_nome

with open(nome_arquivo, "w") as arquivo:
            json.dump(livro, arquivo, indent=4)
"""
"""
with open(nome_arquivo, "r") as arquivo:
            livro_para_excluir = int(input("Digite o ID do produto: "))
            livro = json.load(arquivo)
            for nome_livro in livro:
                novo_inventario = []
                if livro_para_excluir != nome_livro["id"]:
                    novo_inventario.append(livro)

with open(nome_arquivo, "w") as arquivo:
            json.dump(livro, arquivo, indent=4)
"""
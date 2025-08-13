def lista_terceirao():
    print("Liste as pessoas do terceirão")
    print("Quando terminar digite encerrar")
    
    with open("terceirao.txt", 'w') as terceirao:
        while True:
            aluno = input("Aluno: ")
            if aluno.lower()=="encerrar":
                print("Encerrando chamada")
                break
            terceirao.write(aluno + "\n")

lista_terceirao()
    
def listar_alunos():
    with open("terceirao.txt", 'r') as lista:
        print("----Lista de alunos----")
        for aluno in lista:
            lista = aluno.strip()
            print("aluno: ", aluno)

listar_alunos()
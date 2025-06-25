
def contar_ate_dez():
    for i in range(1,11):
        print(i)

contar_ate_dez()

def repetirNome():
    nome = "Miguel"
    numero = 10
    for _ in range(numero):
        print(nome)

repetirNome()

def somandoNumero():
    soma = 0
    for i in range (1,6):
        Numero = float(input(f"Digite o {i}° numero: "))
        soma += Numero
    print("A soma dos 5 numeros é: ", soma)

somandoNumero()

def tabuada():
    x = valor
    print(f"tabuada do {x}")
    for i in range (1,11):
        resultado = x * i
        print(f"{x}x{i} = {resultado}")

valor = int(input("Digite o seu numero: "))
tabuada()

def pares():
    for i in range (2,21,2):
        print(i)

pares()
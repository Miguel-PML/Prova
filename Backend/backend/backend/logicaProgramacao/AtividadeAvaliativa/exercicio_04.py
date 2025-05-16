
def tabuada():
    x = valor
    print(f"tabuada do {x}")
    for i in range (1,11):
        resultado = x * i
        print(f"{x}x{i} = {resultado}")

valor = int(input("Digite o seu numero: "))
tabuada()

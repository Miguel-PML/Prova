valor1 = int(input("Digte o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if(valor1 > valor2):
    print("O valor1 é maior que o valor2")

elif(valor2 > valor1):
    print("O valor2 é maior que o valor1")

else:
    print("Os valores são iguais")

idade = int(input("Qual a sua idade?: "))

if(idade >= 16):
    print("Pode votar")

else:
    print("Não pode votar")

numero = int(input("Digite um numero: "))

if(numero >= 1):
    print("Numero positivo")

elif(numero <= -1):
    print("Numero negativo")

else:
    print("O numero é zero")

mul = int(input("Digite um número: "))


if((mul %3) == 0 and (mul %5) == 0 ):
    print("Ele é multiplo de 3 e 5")

else:
    print("Não é multiplo")
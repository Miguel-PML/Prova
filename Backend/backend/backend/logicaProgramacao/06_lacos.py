#for
for i in range(1, 11):
    print("o valor é", i)

#pares
numeros = [10,15,22,33,42,55,60,73,88,91,100]
pares = 0

for x in numeros:
    if(x%2==0):
        pares += 1

print("Valor de pares é: ", pares)

#somar números

valor = 1
soma = 0
while valor != 0:
    valor = int(input("Digite seu valor: "))
    soma+=valor


print("A soma é: ", soma)






#while
senha = ""
while senha != "Suma":
    senha = input("Digite a senha: ")
    print("Errado")

print("Acesso liberado")




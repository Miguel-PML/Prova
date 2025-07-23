salario = float(input("Digite seu salário: "))
salarioAnual = salario * 12
print("O total de salário anual é: ", salarioAnual)

if(salario >= 5000):
    imposto = salario * 12 / 100 
    print("O imposto é: ", imposto)

elif(salario >= 2000):
    imposto = salario * 7 / 100 
    print("O imposto é: ", imposto)

else:
    imposto = salario * 3 / 100
    print("O imposto é: ", imposto)


impostoAnual = imposto * 12
print("O total de imposto anual é: ", impostoAnual)

#Ex 2
valor=1
soma=0

while valor != 0:
    escolha = input("digite v para subtrair e f para somar: ")

    if(escolha == "v" or escolha == "V"):

            valor = int(input("Digite seu valor: "))
            soma += valor
            print("A soma é: ", soma)


    elif(escolha == "f" or escolha == "F"):
            valor = int(input("Digite seu valor: "))
            soma -= valor
            print("A soma é: ", soma)

    else:
        print("Erro")
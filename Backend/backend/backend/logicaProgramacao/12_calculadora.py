num1 = int(input("Digite o número: "))
num2 = int(input("Digite o número: "))
operacao = input("Digite o tipo de operação: ")

match operacao:
    case "+":
        soma = num1 + num2
        print("Soma = ",soma)

    case "/":
        divisao = num1 / num2
        print("Divisão = ",divisao)

    case "-":
        subtracao = num1 - num2
        print("Subtração = ", subtracao)

    case "*":
        multiplicacao = num1 * num2
        print("Multipicação", multiplicacao)

idade = int(input("Digite a sua idade: "))


match idade:
    case idade if idade <=12:
        print("Vai ir comer terra criança")

    case idade if idade >12 and idade <18:
        print("Insuportavel")

    case idade if idade >18 and idade <60:
        print("Criança com cartão de crédito")

    case idade if idade >60 and idade <100:
        print("O que que á velhinho")

    case idade if idade >100:
        print("Provavelmente vc está prestes a morrer")

    case _:
        print("Idade invalida")

nota = int(input("Digite a sua nota: "))

match nota:
    case 10:
        print("Parabéns")

    case 7|8|9:
        print("Aprovado")
    
    case 0|1|2|3|4|5|6:
        print("Burro")

    case _:
        print("Nota invalida")

import random

secreto = random.randint(1,10)
resposta = 0
while resposta != secreto:

    resposta = int(input("Digite uma resposta: "))

    if(resposta < secreto):
        print("Muito baixo")
    
    elif(resposta > secreto):
        print("Muito alto")

    else:
        print("Correto")

print("Parabéns")


numeros = [14, 30, 24, 4, 15]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número da lista é:", maior)

# Faça um programa que imprima na tela a tabuada de 1 a 10.

for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
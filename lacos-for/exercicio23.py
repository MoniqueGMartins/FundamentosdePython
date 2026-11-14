# Faça um programa que imprima na tela a tabuada de um número qualquer escolhido pelo usuário.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
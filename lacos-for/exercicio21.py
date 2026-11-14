# Faça um programa que receba 15 números inteiros e imprima na tela a somatória dos 15 números.
soma = 0

for i in range(15):
    numero = int(input("Digite um numero inteiro: "))
    soma += numero

print(f"A soma dos 15 números é: {soma}")
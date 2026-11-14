# Solicite dois números e apresente os resultados da soma, subtração, multiplicação e divisão. Considere o segundo número diferente de zero.

#Entrada
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

#Processamento
if numero2 != 0:
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

#Saída
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
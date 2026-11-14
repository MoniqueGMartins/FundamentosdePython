# Solicite um número inteiro e apresente o número anterior e o próximo número.

#Entrada
numero = int(input("Digite um número: "))

#Processamento
antecessor = numero - 1
sucessor = numero + 1

#Saída
print (f"O antecessor de {numero} é {antecessor}")
print (f"O sucessor de {numero} é {sucessor}")
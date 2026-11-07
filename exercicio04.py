# Receba nome, peso e altura. Calcule IMC.

#Entrada
nome =  input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#Processamento
imc = peso / (altura * altura)

#Saída
print(f"{nome} seu IMC é : {imc:.2f}")
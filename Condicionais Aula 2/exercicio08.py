# Faça um programa que receba o nome, cargo e salário de um funcionário. Se o funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final exiba o nome, o cargo e o salário desse funcionário.

#Entrada
nome =  input("Digite o seu nome: ")
cargo = input("Digite o seu cargo: ")
salario = float(input("Digite o seu salário: "))

#Processamento
print(f"Nome: {nome}")
print(f"Cargo: {cargo}")

if salario <= 1000:
    aumento = salario * 0.10
    novoSalario = salario + aumento
    print(f"Seu novo salário é: R$ {novoSalario:.2f}")

else:
    print("Salário sem direito ao reajuste")

#Saída   
print("Fim do programa")


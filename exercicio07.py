# Receba nome, cargo e salário e acrescente 10%

#Entrada
nome =  input("Digite o seu nome: ")
cargo = input("Digite o seu cargo: ")
salario = float(input("Digite o seu salário: "))

#Processamento
aumento = salario * 0.10
novoSalario = salario + aumento

#Saída
print(f" Nome: {nome}")
print(f" Cargo: {cargo}")
print(f" Seu novo salário é: R$ {novoSalario}")


# Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a 500 reais. Escreva um programa que receba o salário de um funcionário e imprima o valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a aumento.
print()
print()
print("******************************")
print("|     Programa Reajuste      |")
print("******************************")
print()
print()

#Entrada
salario = float(input("Digite o seu salário: "))

#Processamento
if salario <= 500:
    aumento = salario * 0.30
    novoSalario = salario + aumento
    print(f"Salário reajustado: R$ {novoSalario}")

else :
    print(f"Funcionáio não tem direito a aumento.")

#Saída   
print("Fim do programa")
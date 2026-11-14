#Receba ano de nascimento e ano atual. Calcule idade e semanas.

#Entrada
anoDeNascimento = int(input("Digite o ano que você nasceu: "))
anoAtual = int(input("Digite o ano atual: "))

#Processamento
idade = anoAtual - anoDeNascimento
idadeEmSemanas = 4 * 12 * idade

#Saída
print(f"Sua idade é: {idade} anos")
print(f"Sua idade em semanas é : {idadeEmSemanas} semanas")


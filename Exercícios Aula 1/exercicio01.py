#Receba a idade em anos e imprima em meses, dias, horas e minutos

#Padrões de escrita de variáveis(Pascal Case, Camel Case, Snake Case, Kebab Case)

#Entrada
idade = int(input("Digite a idade: ")) #Int: Pega o texto e converte para número inteiro

#Processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

#Saída
print() #pular linha
print(f"Sua idade em meses é: {idadeEmMeses} meses")
print(f"Sua idade em dias é: {idadeEmDias} dias")
print(f"Sua idade em horas é: {idadeEmHoras} horas")
print(f"Sua idade em minutos é: {idadeEmMinutos} minutos")


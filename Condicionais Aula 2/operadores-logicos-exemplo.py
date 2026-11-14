#Operadores Lógicos
# and - ambas as expressões devem retornar verdadeiras
# or - basta apenas uma das expressões retornar verdadeira
# not - inverte o resultado da expressão lógica

idade = int(input("Qual é sua idade? "))
ingresso = input("Você tem ingresso? ") #s/n

#Conjugar com o operador AND
if idade >= 18 and ingresso == "s":
    print("Seja bem-vindo à festa 🥳")
else :
    print("Você não pode entrar na festa 🙁")
# Elabore um programa para cálculo de preços de produtos que solicite o preço de compra do produto e o percentual a ser aplicado em cima desse valor para a venda. Calcule e exiba o preço de venda do produto. Se o percentual a ser aplicado for inferior a 50%, exiba uma mensagem informando ao usuário que o produto será vendido com uma margem muito pequena de lucro.
print()
print()
print("******************************")
print("|     Venda com Reajuste      |")
print("******************************")
print()
print()
#Entrada
precoCompra = float(input("Digite o preço de compra do produto: "))
percentualAplicado = float(input("Digite o percentual a ser aplicado: "))

#Processamento
precoVenda = precoCompra + (precoCompra * percentualAplicado /100) #Calcula o percentual

print(f"Preço de Venda: R$ {precoVenda}")

if percentualAplicado < 50:
    print("Atenção! Percentual inferior a 50%. O produto será vendido com uma margem muito pequena de lucro.")

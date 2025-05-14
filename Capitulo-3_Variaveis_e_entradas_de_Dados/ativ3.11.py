#Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o per-
# centual de desconto. Exiba o valor do desconto e o preço a pagar.

precoMercadoria = float(input('Apresente o valor atual da mercadoria para efetuar o desconto:\n'))
descontoMercadoria = float(input('Insira o valor percentual em "%" do desconto que deseja efetuar:\n'))

resultado = (precoMercadoria - (precoMercadoria * descontoMercadoria / 100))

print(f"O Valor de:\n R${precoMercadoria}\n com o desconto apresentado de:\n {descontoMercadoria}% será de\n R${resultado}")


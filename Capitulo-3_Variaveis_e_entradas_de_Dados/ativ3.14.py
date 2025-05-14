# Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por km rodado.

#Entrada de dados 

qtd_Km = float(input('Quantos kilometros o carro percorreu?:\n'))

qtd_Dias = int(input('Informe a quantidade de dias que o carro esteve alugado:\n'))


#Manipulação de Dados
valorTotal = (qtd_Dias * 60) + (0.15 * qtd_Km)


#Saida 
print(f'O valor total a pagar pelo aluguel do carro é de {valorTotal} \n Quantidade total de dias de aluguel do Veiculo: {qtd_Dias}\nQuantidade de Kilometros rodados:{qtd_Km} Kilometros')
      

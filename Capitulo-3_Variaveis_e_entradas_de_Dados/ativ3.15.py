#Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
#um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
#ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o total em dias."""

qtd_Cigarros = int(input('Informe a quantidade de cigarros fumados por dia: '))
qtd_Anos = int(input('Informe a quatidade de anos que ja fumou cigarro: '))


#o total de tempo em minutos que o fumante fumou durante todo o tempo dividido pelo tempo em minutos
totalDiasPerdidos = (qtd_Anos * 365 * qtd_Cigarros * 10) / 1440
print(f'O total de dias perdidos foi de {round(totalDiasPerdidos)} DIAS ')


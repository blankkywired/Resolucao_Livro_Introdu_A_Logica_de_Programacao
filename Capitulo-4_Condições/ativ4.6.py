"""Exercício 4.6
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas."""

distanciaViagem = float(input('Informe a distancia que será percorrida na viagem: '))

#Viagem de ate 200Km
if distanciaViagem <= 200:
    taxa = 0.50
    print(f'O valor da taxa a ser paga será de: R$ {distanciaViagem * taxa}')


#Viagens acima de 200km
else:
    taxa = 0.45
    print(f'O valor da taxa a ser paga será de: R$ {distanciaViagem * taxa}')
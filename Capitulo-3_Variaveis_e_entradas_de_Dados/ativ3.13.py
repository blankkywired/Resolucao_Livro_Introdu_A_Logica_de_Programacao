# Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
# °C em °F. A fórmula para essa conversão é:

temperatura = float(input('Informe a temperatura que deseja converter:\n'))

conversor = ((9 * temperatura) / 5) + 32

print(f'A temperatura {temperatura} C para Fahrenheint é de {conversor} F')


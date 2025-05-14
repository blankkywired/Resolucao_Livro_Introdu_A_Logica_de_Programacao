# Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos.

# Entrada de dados

qtd_Dias = int(input('Insira a quantidade de Dias:\n'))
qtd_Horas = int(input('Quantidade de Horas:\n'))
qtd_Minutos = int(input('Insira aqui a quantidade de minutos:\n'))
qtd_Segundos = int(input('Insira a quantidade de segundos\n'))

# MCOnversão de Dados de Dados
# (Dia = 24h * 60 min * 60 s) (Horas = 60 min * 60s)  (Minutos = 1 * 60s)
total = (qtd_Dias * 24 * 60 * 60) + (qtd_Horas * 60 * 60) + (qtd_Minutos * 60) + qtd_Segundos

# Saida de Dados
print(f'O total de segundos para:\n{qtd_Dias}DIAS \n{qtd_Horas}Horas \n{qtd_Minutos} MINUTOS \n{qtd_Segundos} SEGUNDOS foi de :\n{total} SEGUNDOS')


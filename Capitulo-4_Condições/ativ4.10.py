"""Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
lação: R para residências, I para indústrias e C para comércios. Calcule o preço a
pagar de acordo com a tabela a seguir."""

quantidade_kWh = float(input('Informe a  quantidade de KiloWaths consumida\n:'))
tipoInstalacao = input('Escolha o tipo de instalação:\n[R} - Residencias\n[I] - Industrias\n[C] - Comercios\n>>>>Insira o tipo de instalação abaixo<<<<<\n:')

#Tipo Residencial
if tipoInstalacao == 'R':
    if quantidade_kWh <= 500:
        valor = 0.40
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR$ {round((valor * quantidade_kWh) , 3)} ')
    else:
        valor = 0.65
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR${round((valor * quantidade_kWh) , 3)}')
#Tipo Comercial
elif tipoInstalacao == 'C':
    if quantidade_kWh <= 1000:
        valor = 0.55
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR${round((valor * quantidade_kWh) , 3)}')
    else:
        valor = 0.60
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR${round((valor * quantidade_kWh) , 3)}')
#Tipo industrial
elif tipoInstalacao == 'I':
    if quantidade_kWh <= 5000:
        valor = 0.55
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR${round((valor * quantidade_kWh) , 3)}')
    else:
        valor = 0.60
        print(f'O valor a pagar pela quantidade {quantidade_kWh} kWh é de\nR${round((valor * quantidade_kWh) , 3)}')
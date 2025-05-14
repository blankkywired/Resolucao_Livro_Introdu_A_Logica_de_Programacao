"""Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4."""

number_1 = int(input('Escolha o primeiro numero\n>'))
number_2 = int(input('Escolha o segundo número\n>'))

contador = 0
resultado = 0

while contador < number_1: #Condiçao
    contador += 1
    resultado += number_2 #O resultado vai armazenar todos valores do segundo numero repetindo-os N vezes ( ex : 5 + 5 + 5 + 5 )
print(f'O resultado da multiplicação de {number_1} X {number_2} é\n:{resultado}')






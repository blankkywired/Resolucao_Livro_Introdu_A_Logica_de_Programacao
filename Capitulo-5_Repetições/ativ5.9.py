"""Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
que podemos subtrair 4 cinco vezes de 20."""


n1 = int(input('Insira um numero\n>:'))
n2 = int(input('Insira outro numero\n>:'))


while True:
    resultado = n1 - n2
    print(resultado)
    acumulador = resultado
    resultado = acumulador - n2
    print(resultado)
    if resultado == 0:
     break


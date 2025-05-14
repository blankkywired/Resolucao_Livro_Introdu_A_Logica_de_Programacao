# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
# e o menor.


# Entrada de dados
n1 = float(input('Digite N1: '))
n2 = float(input('Digite N2: '))
n3 = float(input('Digite N3: '))

#Checagem de maior numero
if n1 > n2 and n1 > n3:
    print(f'O maior valor é {n1}')

if n2 > n1 and n2 > n3:
    print(f'O maior valor é {n2}')

if n3 > n1 and n3 > n2:
    print(f'O maior valor é {n3}')


#Checagem de menor numero 
if n1 < n2 and n1 < n3:
    print(f'O menor valor é: {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor valor é: {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor valor é: {n3}')


"""Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
digitado pelo usuário, mas, dessa vez, apenas os números ímpares."""

fim = int(input('Digite o ultimo numero a imprimir\n:'))

x = 0

while x < fim:
    x = x + 1
    if x % 2 !=  0:
        print(x)


        

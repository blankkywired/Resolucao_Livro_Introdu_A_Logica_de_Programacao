"""Exercício 5.7 Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10."""

#Usando laço de repetição FOR
inicio = int(input('Digite um numero para dar inicio a tabuada\n:'))
fim = int(input("digite um numero para dar fim a tabuada\n:"))
fator1 = int(input('Escolha o primeiro fator da tabuada, de 1 a N\n: '))

for i in range(inicio  , fim + 1):
    
    print(fator1 , "x" , i  , "=" , (fator1 * i))



"""Exercício 5.3 Faça um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela."""

contagem = 11
while contagem > 0:
    contagem -= 1 #contagem = contagem - 1
    print(contagem)
print('FOGO !')


for i in range(10, -1, -1):
    print(i)
print('Fogo')

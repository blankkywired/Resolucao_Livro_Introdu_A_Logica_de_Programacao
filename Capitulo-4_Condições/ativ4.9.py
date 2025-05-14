"""Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar."""



print('\t>>>>>>>>>>CALCULADORA DE EMPRESTIMO BANCARIO<<<<<<<<<<\n')
valorCasa = float(input('Qual é o valor da CASA?\n:'))
salario = float(input('Informe o valor do seu salário atual\n:'))
qtd_anos = int(input('Insira a quantidade de anos que deseja fazer o emprestimo da casa\n:'))

limite_prestacao = 0.30 * salario

prestacao = valorCasa / (qtd_anos * 12)

if prestacao <=  limite_prestacao:
    print(f'Emprestimo bancario Autorizado!\nValor da prestação a pagar:\n R${prestacao:.2f}\n Porcentagem(30%) do salário:\n R${limite_prestacao}')

else:
    print(f'Emprestimo bancario Negado!\nValor da prestação:\n R$ {prestacao:.2f}\n Porcentagem(30%) do salario:\n R${limite_prestacao}')


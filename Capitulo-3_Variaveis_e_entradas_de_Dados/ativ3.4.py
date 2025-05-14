# Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não
# pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
# R$ 1.200,00.

# Entrada de dados do usuario
salario = float(input('Insira o salario:\n'))


# Checando a condição do salariodo usuario
if salario > 1200.0:
    print(f'Precisa pagar imposto, salario atual de R$; {salario}' )

else:
    print(f'Isento de pagar imposto , salario atual de R$: {salario}')
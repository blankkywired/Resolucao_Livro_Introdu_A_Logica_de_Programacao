# Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário.

salarioFuncionario = float(input('Apresente o valor  atual do salario do funcionario;\n'))
aumentoSalario = float(input("Informe o valor percentual em '%' do aumento do salario do funcionario:\n"))

resultado = (salarioFuncionario + (salarioFuncionario * aumentoSalario / 100))

print(f"O valor do atual salario é de R$ {salarioFuncionario}\nApós o aumento de {aumentoSalario}% sera de R$ {resultado}")


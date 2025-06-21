#Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança.Exiba os valores mes a mes para os 24 primeiros meses.
#Escreva o total ganho com juros no periodo

valorDepositoInicial = float(input('Qual será o valor inicial do seu deposito?: '))
jurosTaxa = int(input('Informe-nos a taxa de juros dessa poupança: '))

mesesDoANo = {
    "mes": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
}

jurosAcumulador = 0
jurosDeposito = (jurosTaxa / 100) * valorDepositoInicial 
#Associando a variavel i como um index percorrendo cada elemento dentro da key mes do dicionario mesesDoAno
for j in range(0,2):
    for i in mesesDoANo['mes']:  # --- > Para i dentro de mesesDoAno, dentro da lista "mes"
        print(i , valorDepositoInicial + jurosAcumulador , 'R$' )
        print("")
        jurosAcumulador += jurosDeposito # a cada iteração o acumulador adiciona o valor da taxa de juros do preço do deposito inicial
    print(20 * "-")
valorGanho = jurosAcumulador
print(f'O valor total ganho de juros é de {valorGanho} R$')

    #Explicação: Se o valor do deposito inicial foi 400 R$, e a taxa é 5% sob o valor do deposito, entao a taxa sera 20 R$, o valor a ser pago a cada mes sera o valor inicial para pagar(400 r$) + valor do juros 

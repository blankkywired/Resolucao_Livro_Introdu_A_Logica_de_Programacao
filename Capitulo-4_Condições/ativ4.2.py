# Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h.


velocidadeCarro = float(input('Qual é a velocidade do carro?; '))

#A multa sera dada pela diferença entre a velocidade acima de 80 e a velocidade maxima tolerada

if velocidadeCarro > 80:
    multa = (velocidadeCarro - 80) * 5
    print('Voce vai pagar a  multa no valor de \n: R$' , multa)




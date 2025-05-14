# Exercício 4.5
# Execute o programa (Listagem 4.5) e experimente alguns valores.
# Verifique se os resultados foram os mesmos do programa anterior (Listagem 4.3).

idadeCarro = int(input('Insira a idade do seu carro: '))


#Checagem de condições
if idadeCarro > 0 and idadeCarro <= 3 :
    print('Seu carro é novo!')
elif idadeCarro < 0:
    print('Insira um valor valido')
elif idadeCarro > 3:
    print('Seu carro ja está velho')
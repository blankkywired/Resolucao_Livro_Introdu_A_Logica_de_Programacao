fator1 = int(input('Escolha um numero\n:'))
fator2 = 0 
while fator2 < 10:
    produto = 0
    while produto < (fator1 * 10):
        produto += 1
        if produto % fator1 == 0:
            fator2 += 1
            print(fator1 , "X", fator2, "=", produto)



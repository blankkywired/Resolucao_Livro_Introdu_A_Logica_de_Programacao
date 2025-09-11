sequencia = list(range(0, 20)) #Cria uma lista padronizada de tamanho determinado pela função range

#print(sequencia)
for i in sequencia:
    if i == 10: #Ignora o valor 10 e prossegue com a iteração sob os valores da lista
        continue
    else:
        print(i)


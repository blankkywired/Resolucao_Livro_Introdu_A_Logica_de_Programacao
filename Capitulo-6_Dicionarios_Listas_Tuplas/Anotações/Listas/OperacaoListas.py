ListaNum = [0, 3, 5, 7, 9]
valorMaximo = ListaNum[0]
#Valor Maximo
for valor in ListaNum:
    if valor > valorMaximo:
        valorMaximo = valor
print(valorMaximo)

#Procurar valor minimo
valorMin = ListaNum[0]
for i in ListaNum:
    if i < valorMin:
        valorMin = i

print(valorMin)
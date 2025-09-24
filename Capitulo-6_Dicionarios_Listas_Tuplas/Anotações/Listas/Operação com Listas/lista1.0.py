valores = [1, 2, 3, 11,  4, 5, 6]
indiceMaximo = valores[0]

for numero in valores:
    if numero > indiceMaximo:
        indiceMaximo = numero

print(indiceMaximo)

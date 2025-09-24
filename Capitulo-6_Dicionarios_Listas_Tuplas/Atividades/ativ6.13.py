temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]

def menor_temp(lista):
    valorMinimo = temperaturas[0]
    for temperatura in temperaturas:
        if temperatura < valorMinimo:
            valorMinimo = temperatura
    return valorMinimo

def maior_temp(lista):
    valorMaximo = temperaturas[0]
    for temperatura in temperaturas:
        if temperatura > valorMaximo:
            valorMaximo = temperatura
    return valorMaximo

def media_temp(lista):
    numero_elementos = len(temperaturas)
    totalSum = sum(temperaturas)
    media = totalSum / numero_elementos
    return media

print(f'A menor temperatura da lista é: {menor_temp(temperaturas)} Graus')
print(f'A maior temperatura da lista é: {maior_temp(temperaturas)} Graus')
print(f'A media das temperaturas da lista é: {media_temp(temperaturas)} Graus ')


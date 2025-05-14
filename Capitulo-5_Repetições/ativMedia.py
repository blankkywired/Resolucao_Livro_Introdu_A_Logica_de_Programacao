quantidade_caractere = 0
soma = 0 

inicio_fim = True #Condição que ira determinar se o algoritmo prossegue ou para

while inicio_fim:
    numero = int(input('Digite um numero, digite 0 para parar o loop: ')) #numero de entrada do usuario
    soma += numero
    if numero != 0: 
        quantidade_caractere += 1
    media = soma / quantidade_caractere

    if numero == 0:
        inicio_fim = False
print(media)


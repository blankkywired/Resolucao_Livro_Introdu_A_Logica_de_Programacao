#Escreva um programa que leia todos os numeros do teclado. O programa deve ler todos os numeros ate que o usuario digite zero. No final da execução,
#exiba a soma e a media aritmetica

acumulador = 0
quantidade_fatores_digitados = 0

iniciar = True

while iniciar:
    numeroUsuario = float(input('Informe um numero: '))
    acumulador += numeroUsuario
    quantidade_fatores_digitados += 1

    if numeroUsuario == 0:
        print(f'A media é: {acumulador /(quantidade_fatores_digitados - 1)}\nQuantidade numeros digitados: {quantidade_fatores_digitados - 1}' )
        iniciar = False
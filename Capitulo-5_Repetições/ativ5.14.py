#Escreva UM PROGRAMA QUE LEIA TODOS OS NUMEROS DO TECLADO. o PROGRAMA DEVE LER TODOS OS NUMEROS ATE QUE O USUARIO DIGITE ZERO. nO FINAL DA EXECUÇÃO,
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
        
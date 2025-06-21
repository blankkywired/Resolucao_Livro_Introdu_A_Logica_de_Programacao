
iniciar = True

while iniciar:
    escolha_Opcao = int(input('''Escolha uma opção:
[1] - Adição
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
[5] - Sair
: '''))

    
    if escolha_Opcao == 1:
        print(20 * "_")
        for i in range(0, 10):
            for j in range(0, 11):
                print(f'{i} + {j} = {i + j}')
            print(20 * "_")

    elif escolha_Opcao == 2:
        print(20 * "-")
        for i in range(0 , 11 ):
            for j in range(0, 11):
                print(f'{i} - {j} = {i - j}')
            print(20 * "-")
            
    elif escolha_Opcao == 3:
        print(20 * "-")
        for i in range(0, 11):
            for j in range(0, 11):
                print(f'{i} * {j} = {i * j}')
            print(20 * "-")

    elif escolha_Opcao == 4:
        print(20 * "-")
        for i in range(0, 11):
            for j in range(0, 11):
                if j != 0:
                    print(f'{i} / {j} = {i / j}')
            print(20 * "-")
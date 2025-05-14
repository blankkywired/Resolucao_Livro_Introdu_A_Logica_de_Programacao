"""Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada."""

n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

print("""

                                                                                                                                             
      _____          ____    ____              _____    ____   ____  ____               ____   _________________       _____         _____   
  ___|\    \    ____|\   \  |    |         ___|\    \  |    | |    ||    |         ____|\   \ /                 \ ____|\    \    ___|\    \  
 /    /\    \  /    /\    \ |    |        /    /\    \ |    | |    ||    |        /    /\    \\______     ______//     /\    \  |    |\    \ 
|    |  |    ||    |  |    ||    |       |    |  |    ||    | |    ||    |       |    |  |    |  \( /    /  )/  /     /  \    \ |    | |    |
|    |  |____||    |__|    ||    |  ____ |    |  |____||    | |    ||    |  ____ |    |__|    |   ' |   |   '  |     |    |    ||    |/____/ 
|    |   ____ |    .--.    ||    | |    ||    |   ____ |    | |    ||    | |    ||    .--.    |     |   |      |     |    |    ||    |\    \ 
|    |  |    ||    |  |    ||    | |    ||    |  |    ||    | |    ||    | |    ||    |  |    |    /   //      |\     \  /    /||    | |    |
|\ ___\/    /||____|  |____||____|/____/||\ ___\/    /||\___\_|____||____|/____/||____|  |____|   /___//       | \_____\/____/ ||____| |____|
| |   /____/ ||    |  |    ||    |     ||| |   /____/ || |    |    ||    |     |||    |  |    |  |`   |         \ |    ||    | /|    | |    |
 \|___|    | /|____|  |____||____|_____|/ \|___|    | / \|____|____||____|_____|/|____|  |____|  |____|          \|____||____|/ |____| |____|
   \( |____|/   \(      )/    \(    )/      \( |____|/     \(   )/    \(    )/     \(      )/      \(               \(    )/      \(     )/  
    '   )/       '      '      '    '        '   )/         '   '      '    '       '      '        '                '    '        '     '   
        '                                        '                                                                                           



""")

operacao = int(input('Qual operação voce quer realizar? \n1 --- [+}Soma \n2 --- [-]Subtração \n3 --- [*] Multiplicação \n4 --- [/] Divisão\n: '))

if operacao == 1:
    print(f'Soma: {n1 + n2}')
else:
    if operacao == 2:
        print(f'Subtracao: {n1 - n2}')
    else:
         if operacao == 3:
            print(f'Multiplicação: {n1 * n2}')
         else:
            if operacao == 4:
                print(f'Divisão: {n1 / n2}')
            else:
                print('Ops, parece que deu algo errado\nEscolha uma operação aritmetica válida')
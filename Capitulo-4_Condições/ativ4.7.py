"""Exercício 4.7 Rastreie o programa da listagem 4.7. Compare seu resultado ao apre-
sentado na tabela 4.2."""

categoria = int(input('Digite a categoria do Produto: '))

if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print('Cateogira Invalida, digite um valor entre 1 e 5!')
                    preco = 0

print('O preço do produto é de: R$' , preco )


#Algoritmo que simula uma caixa registradora
codigoProdutos = {
    "codigos": [1, 2, 3, 5, 9],
    "valoresPorCodigo": [0.50, 1, 4, 7, 8]
}
valorProdutos = 0
valorTotal_compra = 0
while True:
    codigo_Usuario = int(input('Informe o codigo do produto que voce deseja comprar: '))
    #Exibir o valor total da compra
    if codigo_Usuario == 0:
        print(10 * '-', 'Valor Total da Compra', 10 * '-')
        print(f' R${valorTotal_compra}')   
        break 
    elif codigo_Usuario in codigoProdutos['codigos']:
        quantidadeProduto = int(input('Insira a quantidade deste produto que voce deseja comprar; '))
        indiceBusca = codigoProdutos["codigos"].index(codigo_Usuario)

    #Buscar o valor do produto associado ao indice do codigo informado pelo usuario se este estiver dentro da lista de codigos
        valorProdutos = (codigoProdutos["valoresPorCodigo"][indiceBusca]) * quantidadeProduto
        valorTotal_compra += valorProdutos
        print(30 * '-')
        print(f'Subtotal da compra: R$ {valorTotal_compra}   |')
        print(30 * '-')

    elif codigo_Usuario not in codigoProdutos['codigos']:
        print('Por favor insira um codigo válido:')





#Produto/Quantidade/Valor por unidade
tabela = {"Alface": [1000, 0.45],
          "Batata": [500, 1.20],
          "Tomate": [2001, 2.30],
          "Feijão": [100, 1.50]
}

print(tabela["Alface"][0]) #Output: 1000, chamando a key, depois o elemento associado ao indice 0

#Buscar quantidade
produto_estoque = input(('Qual produto voce quer achar?:'))

if produto_estoque in tabela:
    print(f"No estoque possui {tabela[produto_estoque][0]:.2f} {produto_estoque}")
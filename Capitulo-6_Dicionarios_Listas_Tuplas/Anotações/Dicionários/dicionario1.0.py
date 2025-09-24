tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50
}

for produto in tabela:
    print(produto , tabela[produto]) #mostra key/valor associado a cada key, respectivamente

#Preço do produto:
# tabela[produto] usando o for loop ou entao tabela["Alface"] para ser mais especifico

#Fazer busca em um dicionario com a entrada fornecida pelo usuario
busca = input(('Qual produto voce procura?: '))

if busca in tabela:
    print(F"O produto {busca} custa {tabela[busca]:.2f} R$") #Retorna o valor do produto associado
else:
    print('Este produto não se encontra no estoque no momento')

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

for i in venda:
    produto, valor = i
    print(produto, valor)

#O laço for ira percorrer a lista venda  e o indice i irá assumir os valores de cada elemento dentro da lista (ex: tomate , 5 representam um unico elemento)
#Ja produto e valor servem para dividir o indice i em dois pedaços, assim, ao chamarmos no print, o produto ira receber o primeiro elemento de i(tomate), e valor vai
#RECEBER O SEGUNDO VALOR DE I(5)

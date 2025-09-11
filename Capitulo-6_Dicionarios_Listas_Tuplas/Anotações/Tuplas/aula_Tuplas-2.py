#Fatiamento e Indexação de tuplas

tupla = ("a", "b", "c")
print(tupla[1:]) #---> Retorna o valor do começo do intervalo expecificado pelo usuario ate o final da tupla(Output: "b", "c")


tupla = ("a", "b", "c", "d", "e", "f")
print(tupla[2:4])
#-->Retorna o valor do começo do intervalo expecificado pelo usuario ate o final da tupla(Output: "c", "d", )
#Por que so retorna "c" e "d" e nao "c", "d" e "e?" O segundo numero especificado no intervalo serve 
# para mostrar o proximo elemento dentro do intervalo uma casa a menos, para compensar isso, se adiciona uma unidade a mais da posição do elemento na tupla

print(tupla[2:5])
#Output : "c", "d" , "e"



#Multiplicar/Repetir valores de uma tupla
tuplaRepeticao = "A" , "B", "C"
print(tuplaRepeticao * 2)
#Output: ('A', 'B', 'C', 'A', 'B', 'C')

#Quantidade de elementos de uma tupla
print(len(tuplaRepeticao))


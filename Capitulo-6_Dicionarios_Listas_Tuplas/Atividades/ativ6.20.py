<<<<<<< HEAD
#Algoritmo que recebe uma palavra do usuario e retorna o valor de cada caracteres uma unica com ver a quantidade de incidencias

# que o caractere aparece na respectiva palavra

palavraUsuario = str(input('Insira uma palavra qualquer:\n'))
dicionarioCaracter = {}
for letra in palavraUsuario:
    if letra in dicionarioCaracter:
        dicionarioCaracter[letra] = dicionarioCaracter[letra] + 1 # -- > Adiciona + 1 com base na key do dicionario, cada letra será uma key, e a quantidade de ocorrencias o seu valor
    else:
        dicionarioCaracter[letra] =  1 #--> Se a letra n estiver repetida no dicionario, entao sua ocorrencia será apenas uma unica vez
print(dicionarioCaracter)

a = {1, 2, 3, 4}
b = {5, 6, 7, 8}

=======
#Algoritmo que recebe uma palavra do usuario e retorna o valor de cada caracteres uma unica com ver a quantidade de incidencias

# que o caractere aparece na respectiva palavra

palavraUsuario = str(input('Insira uma palavra qualquer:\n'))
dicionarioCaracter = {}
for letra in palavraUsuario:
    if letra in dicionarioCaracter:
        dicionarioCaracter[letra] = dicionarioCaracter[letra] + 1 # -- > Adiciona + 1 com base na key do dicionario, cada letra será uma key, e a quantidade de ocorrencias o seu valor
    else:
        dicionarioCaracter[letra] =  1 #--> Se a letra n estiver repetida no dicionario, entao sua ocorrencia será apenas uma unica vez
print(dicionarioCaracter)

a = {1, 2, 3, 4}
b = {5, 6, 7, 8}

>>>>>>> 476e67a (Added new files to path)
print(a | b)
"""Exercício 5.10 Modifique o programa da listagem 5.10 para que aceite respostas
com letras maiúsculas e minúsculas em todas as questões."""


ponto = 0
questao = 1
while questao <= 3:
    resposta = input(f'Resposta da questao {questao} : ' )

    if questao == 1 and (resposta == "b" or resposta == 'B'):
        ponto = ponto + 1
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        ponto = ponto + 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        ponto = ponto + 1
    
    questao += 1
print(f'O aluno fez {ponto} pontos')

#Cada vez que o aluno responder uma questão será adicionado +1 a variavel questao e repetindo o laço while enqunanto a questão for menor ou 
#igual a 3


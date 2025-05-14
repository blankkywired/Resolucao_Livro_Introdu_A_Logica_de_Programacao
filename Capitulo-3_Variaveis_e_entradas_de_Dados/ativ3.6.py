# Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi
# ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
# que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
# está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.



#Entrada de dados(nota do Aluno)
nota1 = float(input('Digite a primeira nota do Aluno;\n'))
nota2 = float(input('Digite a segunda nota:\n'))
nota3 = float(input('Digite a terceira nota:\n'))


# Checando entradas de dados

if nota1 > 7 and nota2 > 7 and nota3 > 7:  #Todas as notas(materia1 , materia2 e materia3 ) devem ser maiores do que 7
    print('Aluno Aprovado')
else:
    print(f'Aluno reprovado, notas insuficientes NOTAS: \n {nota1} \n {nota2} \n {nota3}')
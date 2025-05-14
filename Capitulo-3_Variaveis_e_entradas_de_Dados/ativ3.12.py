# Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Qual a distancia da viagem?:\n')) #Kilmetro > Metro
velocidadeMedia = float(input('Qual é a velocidade media: ')) #M/s

# Distancia em Km convertido para Metros
tempo  = (distancia * 1000) / velocidadeMedia

#Arredondando valor 
resultado = round(tempo, 0)
print(f'O tempo da viagem sera de: {resultado} Segundos')




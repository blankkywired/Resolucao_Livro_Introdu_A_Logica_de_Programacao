base = int(input('Digite o tamanho da base do triangulo retangulo\n:'))
contador = 0
Simbolos = 0
letra = "x"

while contador < base:
    contador += 1
    Simbolos += 1
    triangulo = contador * letra
    print(triangulo ,  "        " , Simbolos , "Simbolos")



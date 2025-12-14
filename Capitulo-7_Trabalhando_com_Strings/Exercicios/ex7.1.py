def ocorrenciaString():
    string_A = input()
    string_B = input()
    return f"Resultado: {string_B} encontrado na posição {string_A.find(string_B)} de {string_A}"

print(ocorrenciaString())
arquivo = open("numeros.txt", "w")

user_text = input(('Digite uma mensagem:'))
arquivo.write(f"{user_text}\n")
arquivo.close()

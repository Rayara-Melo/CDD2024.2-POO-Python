with open("registro.txt", "a") as arquivo:
    texto = input("Digite um texto: ")
    arquivo.write(f"{texto}\n")
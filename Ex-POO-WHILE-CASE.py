while True:
    opcao = int(input("Digite sua opcao: \n"
                      "1 Para GRAVAR:\n"
                      "2 Para LER:\n"
                      "3 Para SAIR:"))
    match opcao:
        case 1:
            texto = input("Digite um texto: ")
            gravarTexto(texto)
        case 2:
            lerTexto()
        case 3:
            break
        case _:
            print("Opção invalida")
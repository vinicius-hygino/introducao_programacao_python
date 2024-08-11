#Modifique o programa 7.2 de forma a utilizar uma lista de palavras. No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula: índice = (numero * 776) % len(lista_palavras)

#Programa 7.2 - Jogo da forca(modificado)

def verifica_inteiro(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("O número deve ser maior ou igual a zero.")
        except Exception:
            print("A entrada deve ser um número.")

lista_de_palavras = ["abacaxi", "manga", "acerola", "banana", "maça", "pera"]
numero = verifica_inteiro("Digite um número: ")
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice]

digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    
    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")

    linha3 = ""
    if erros == 5:
        linha3 += " /  "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")

    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era {palavra}")
        break
#Modifique o programa 7.2 para utilizar listas de strings para desenhar o boneco da forca. Você pode utilizar uma lista para cada linha e organiza-las em uma lista de listas. Em vez de controlar quando imprimir cada parte, desenha nesas listas, substituindo o elemento a desenhar.

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
    
    linha = [
        ["X"," =","=",":","=","="],
        ["X"," "," "," "," "," "],
        ["X"," "," "," "," "," "],
        ["X"," "," "," "," "," "],
        ["X"," "," "," "," "," "]
    ]

    if(erros >= 1):
        linha[1][3] = " 0"
    if(erros == 2):
        linha[2][3] = " |"
    if(erros > 2):
        linha[2][3] = "|"
    if(erros >= 3):
        linha[2][2] = "\-"
    if(erros >= 4):
        linha[2][4] = "-/"
    if(erros >= 5):
        linha[3][3] = " |"
    if(erros >= 6):
        linha[4][2] = " /"
    if(erros >= 7):
        linha[4][4] = "\ "

    for e in linha:
        l = "".join(e)
        print(l)


    if erros == 7:
        print("Enforcado!")
        print(f"A palavra secreta era {palavra}")
        break
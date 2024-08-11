#Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista, também com três elementos.

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def imprime_regras():
    print("Use o seguinte mapa para jogar.")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

def imprime_lista(lista):
    print(f" {lista[0][0]} | {lista[0][1]} | {lista[0][2]}")
    print("---+---+---")
    print(f" {lista[1][0]} | {lista[1][1]} | {lista[1][2]}")
    print("---+---+---")
    print(f" {lista[2][0]} | {lista[2][1]} | {lista[2][2]}")

def verifica_jogada(pergunta,lista_jogadas):
    while True:
        try:
            entrada = int(input(pergunta))
            if(1 <= entrada <= 9) and (entrada not in lista_jogadas):
                return entrada
            else:
                print("A entrada deve ser um número de 1 a 9 que ainda não foi jogado.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_vitoria(lista):
    jogador1_venceu = False
    jogador2_venceu = False
    #jogador 1
    if(lista[0][0] == "x") and (lista[0][1] == "x") and (lista[0][2] == "x"):
        jogador1_venceu = True
    elif(lista[1][0] == "x") and (lista[1][1] == "x") and (lista[1][2] == "x"):
        jogador1_venceu = True
    elif(lista[2][0] == "x") and (lista[2][1] == "x") and (lista[2][2] == "x"):
        jogador1_venceu = True
    
    elif(lista[0][0] == "x") and (lista[1][0] == "x") and (lista[2][0] == "x"):
        jogador1_venceu = True
    elif(lista[0][1] == "x") and (lista[1][1] == "x") and (lista[2][1] == "x"):
        jogador1_venceu = True
    elif(lista[0][2] == "x") and (lista[1][2] == "x") and (lista[2][2] == "x"):
        jogador1_venceu = True
    
    elif(lista[0][0] == "x") and (lista[1][1] == "x") and (lista[2][2] == "x"):
        jogador1_venceu = True
    elif(lista[2][0] == "x") and (lista[1][1] == "x") and (lista[0][2] == "x"):
        jogador1_venceu = True
    
    #jogador2
    if(lista[0][0] == "o") and (lista[0][1] == "o") and (lista[0][2] == "o"):
        jogador2_venceu = True
    elif(lista[1][0] == "o") and (lista[1][1] == "o") and (lista[1][2] == "o"):
        jogador2_venceu = True
    elif(lista[2][0] == "o") and (lista[2][1] == "o") and (lista[2][2] == "o"):
        jogador2_venceu = True
    
    elif(lista[0][0] == "o") and (lista[1][0] == "o") and (lista[2][0] == "o"):
        jogador2_venceu = True
    elif(lista[0][1] == "o") and (lista[1][1] == "o") and (lista[2][1] == "o"):
        jogador2_venceu = True
    elif(lista[0][2] == "o") and (lista[1][2] == "o") and (lista[2][2] == "o"):
        jogador2_venceu = True
    
    elif(lista[0][0] == "o") and (lista[1][1] == "o") and (lista[2][2] == "o"):
        jogador2_venceu = True
    elif(lista[2][0] == "o") and (lista[1][1] == "o") and (lista[0][2] == "o"):
        jogador2_venceu = True

    #empate
    empatou = True
    for e in lista:
        for i in e:
            if(i == " "):
                empatou = False
    
    if(jogador1_venceu == True):
        return 1
    elif(jogador2_venceu == True):
        return 2
    elif(empatou == True):
        return 3
    else:
        return 0

def atualiza_lista(lista, jogada, jogador):
    lista_numerica = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
    if(jogador == 1):
        for x, e in enumerate(lista_numerica):
            for y, i in enumerate(e):
                if(i == jogada):
                    lista[x][y] = "x"
    elif(jogador == 2):
         for x, e in enumerate(lista_numerica):
            for y, i in enumerate(e):
                if(i == jogada):
                    lista[x][y] = "o"
    
    return lista

def tela_de_vitoria(vitoria,lista):
    imprime_lista(lista)
    print("=" * 100)
    if(vitoria == 1):
        print(f"{'Jogador 1 venceu!':^100}")
    elif(vitoria == 2):
        print(f"{'Jogador 2 venceu!':^100}")
    else:
        print(f"{'Velha':^100}")
    print("=" * 100)

def main():
    cabecalho("Jogo da Velha")
    imprime_regras()
    print("-" * 100)
    print()

    lista = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    lista_jogadas = []
    while True:
        imprime_lista(lista)
        
        j1 = verifica_jogada("Jogador 1: ", lista_jogadas)
        lista_jogadas.append(j1)
        lista = atualiza_lista(lista,j1, 1)

        vitoria = verifica_vitoria(lista)
        if(vitoria == 1) or (vitoria == 2) or (vitoria == 3):
            break
        
        imprime_lista(lista)
        
        j2 = verifica_jogada("Jogador 2: ", lista_jogadas)
        lista_jogadas.append(j2)
        lista = atualiza_lista(lista, j2, 2)
        
        vitoria = verifica_vitoria(lista)
        if(vitoria == 1) or (vitoria == 2) or (vitoria == 3):
            break
    
    tela_de_vitoria(vitoria,lista)

main()
        
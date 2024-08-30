#Utilizando a função type, escreva uma função recursiva que imprima os elemetos de uma lista. Cada elemento deve ser impresso separadamente, um por linha. Considere o caso de listas dentro de listas, como L = [1, [2, 3, 4, [5, 6, 7]]]. A cada nível, imprima a lista mais à direita, como fazemos ao identar blocos em Python. Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco à esquerda de cada elemento.

def imprime_lista(lista, nivel = 0):
    for e in lista:
        if(type(e) == list):
            nivel += 1 
            imprime_lista(e, nivel)
        else:
            print(" " * nivel, e)

l = [1, [2, 3, 4, [5, 6, 7]]]
imprime_lista(l)
#Escreva uma função que receba uma string e uma lista. A função deve comprar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

def string_na_lista(string, lista):
    if(string in lista):
        return True
    else:
        return False


def main():
    lista = ["abacate", "maçã", "banana", "coco", "kiwi"]
    string = "abacate"

    print(string_na_lista(string, lista))

main()
#Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
#1ª string: AATTCGAA
#2ª string: TG
#3ª string: AC
#resultado: AAAACCAA

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_string2(pergunta,string1):
    while True:
        string2 = input(pergunta)
        if(string2 in string1):
            return string2
        else:
            print("A primeira palavra não possui essas letras para substituir.")

def verifica_string3(pergunta,string2):
    while True:
        string3 = input(pergunta)
        if(len(string3) == len(string2)):
            return string3
        else:
            print("Digite a mesma quantidade de letras que serão substituidas.")

def main():
    cabecalho("Esse programa substitui letras de uma palavra.")

    string1 = input("Digite a primeira palavra: ")
    string2 = verifica_string2("Digite os caracteres a substituir: ",string1)
    string3 = verifica_string3("Digite o que vai substitui-los: ",string2)

    lista1 = list(string1)
    lista2 = list(string2)
    lista3 = list(string3)
    
    for x, e in enumerate(lista2):
        for y, i in enumerate(lista1):
            if(i == e):
                lista1[y] = lista3[x]
    
    resultado = "".join(lista1)

    print("=" * 100)
    print(f"Resultado = {resultado}")
    print("=" * 100)
    
    

main()
#Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
#1ª string: AATTGGAA
#2ª string: TG
#3ª string: AAAA

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa tira as letras de uma palavra.")

    string1 = input("Digite uma palavra: ")
    string2 = input("Quais letras deseja retirar?: ")

    lista1 = list(string1) #transformo a string em lista para manipula-lá
    lista2 = []
    for e in lista1:
        if(e not in string2): #se o elemento não está na string2(retirar) adiciono na lista 2
            lista2.append(e)
    
    resultado = "".join(lista2) #transformo a nova lista em string

    print("-" * 100)
    print(f"Resultado = {resultado}")
    print("-" * 100)

main()
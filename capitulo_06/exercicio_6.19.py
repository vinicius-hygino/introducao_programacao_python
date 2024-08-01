#Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#Os valores comums às duas listas
#Os valores que só existem na primeira
#Os valores que existem apenas na segunda
#Uma lista com os elementos não repetidos das duas listas
#A primeira lista sem os elementos repetidos na segunda

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa compara duas listas usando conjuntos.")

    lista1 = [1,2,3,4,5]
    lista2 = [5,6,7,8,9]

    conj1 = set(lista1)
    conj2 = set(lista2)

    print("-" * 100)
    print(f"Primeira lista: {lista1}")
    print(f"Segunda lista: {lista2}")
    print("-" * 100)
    
    print(f"Valores comums às duas listas: {conj1 & conj2}")

    print(f"Valores que só existem na primeira: {conj1 - conj2}")

    print(f"Valores que só existem na segunda: {conj2 - conj1}")

    print(f"Lista com elementos não repetidos nas duas listas: {conj1 ^ conj2}")

    print(f"A primeira lista sem elementos repetidos na segunda: {conj1 - conj2}")

main()
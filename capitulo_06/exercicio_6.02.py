#Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def le_lista(n):
    x = 0
    lista = []
    while(x < n):
        entrada = input(f"Elemento {x + 1}: ")
        lista.append(entrada)
        x += 1
    return lista

def junta_listas(lista1, lista2):
    lista = []
    for e in lista1:
        lista.append(e)
    for e in lista2:
        lista.append(e)
    return lista

def main():
    cabecalho("Esse programa junta duas listas em uma terceira.")
    print("Lista 1")
    lista1 = le_lista(5)
    print("Lista 2")
    lista2 = le_lista(5)

    lista3 = junta_listas(lista1, lista2)

    print("=" * 100)
    print(f"Lista 3 = {lista3}")
    print("=" * 100)

main()
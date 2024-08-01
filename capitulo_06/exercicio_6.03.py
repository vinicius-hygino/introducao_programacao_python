#Faça um program que percorra duas listas e gere uma terceira sem elementos repetidos

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def le_listas(n):
    pass

def junta_lista(lista1, lista2):
    lista = []
    for e in lista1:
        if(e not in lista):
            lista.append(e)
    
    for e in lista2:
        if(e not in lista):
            lista.append(e)
    
    return lista

def main():
    cabecalho("Esse programa junta duas listas sem elementos repetidos.")

    lista1 = [1,2,3,4,5]
    lista2 = [4,5,6,7,8,9,10]

    lista3 = junta_lista(lista1, lista2)

    print("=" * 100)
    print(f"Lista final = {lista3}")
    print("=" * 100)

main()
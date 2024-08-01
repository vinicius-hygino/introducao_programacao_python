#Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
#Os elementos que não mudaram
#Os novos elementos
#Os elementos que foram removidos

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    lista1 = [1,2,3,4,5]
    lista2 = [6,2,3,7,8]

    c1 = set(lista1)
    c2 = set(lista2)

    nao_mudaram = c1 & c2
    novos = c2 - c1
    removidos = c1 - c2
    
    print("-" * 100)
    print(f"Lista 1 = {lista1}")
    print(f"Lista 2 = {lista2}")
    print("-" * 100)

    print("=" * 100)
    print(f"Elementos que não mudaram = {nao_mudaram}")
    print(f"Novos elementos = {novos}")
    print(f"Elementos removidos = {removidos}")
    print("=" * 100)

main()

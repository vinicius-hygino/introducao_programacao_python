#Crie um programa que receba uma lista de nomes de arquivo e os imprima, um por um.

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def monta_lista():
    lista = []
    n = 1
    while True:
        nome = input(f"Digite o nome do {n}º arquivo(0 sai): ")
        if(nome == "0"):
            break
        else:
            lista.append(nome)
            n += 1
    return lista

def imprime_lista(lista):
    for x, e in enumerate(lista):
        try:
            with open(e, "r") as arquivo:
                print("\n")
                print(f"{e}")
                print("\n")
                for l in arquivo.readlines():
                    print(l)
        except Exception:
            print(f"Verifique o nome do arquivo {x + 1}")
    

def main():
    cabecalho("Esse programa imprime uma lista de arquivos.")

    lista = monta_lista()

    imprime_lista(lista)

main()


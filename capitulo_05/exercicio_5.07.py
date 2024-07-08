#Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def imprime_multiplo_3(inicio, fim):
    contador = inicio
    while(contador <= fim):
        print(f"3x{contador:<3} = {contador * 3:>3}")
        contador += 1

def main():
    cabecalho("Esse programa imprime n múltiplos de 3")

    inicio = verifica_int("Digite o valor inical: ")
    fim = verifica_int("Digite o valor final: ")
    
    print("=" * 100)
    if(inicio <= fim):
        imprime_multiplo_3(inicio, fim)
    else:
        print("O valor inicial deve ser menor que o final.")
    print("=" * 100)

main()
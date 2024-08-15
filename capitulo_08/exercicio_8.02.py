#Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def verifica_multiplo(n1, n2):
    d = n1 / n2
    if(d % 1 == 0):
        return True
    else:
        return False

def main():
    cabecalho("Esse programa verifica se dois números são multiplos.")

    n1 = verifica_int("Digite o primeiro número: ")
    n2 = verifica_int("Digite o segundo número: ")

    multiplo = verifica_multiplo(n1, n2)

    print("-" * 100)
    if(multiplo == True):
        print(f"{n1} é multiplo de {n2}.")
    else:
        print(f"{n1} não é multiplo de {n2}.")
    print("-" * 100)

main()


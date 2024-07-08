#Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    while True:
        try:
            entrada = input(pergunta)
            if(entrada.isnumeric):
                return entrada
            else:
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número.")


def verifica_palindromo(n):
    #monta uma lista
    lista = []
    for e in n:
        lista.append(e)
    
    #inverte a lista e armazena em outra variavel
    lista2 = []
    x = len(lista) - 1
    while(x >= 0):
        lista2.append(lista[x])
        x -= 1
    
    #compara as listas
    if(lista == lista2):
        return True
    else:
        return False
            

def main():
    cabecalho("Esse programa verifica se um número é palíndromo.")

    n = verifica_entrada("Digite um número: ")


    palindromo = verifica_palindromo(n)

    print("=" * 100)
    if(palindromo == True):
        print(f"{n} é um palíndromo.")
    else:
        print(f"{n} não é um palíndromo.")
    print("=" * 100)

main()
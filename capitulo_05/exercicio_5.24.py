#Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def verifica_primo(n):
    primo = True
    if(n == 0):
        primo = False    
    elif(n == 1):
        primo = False
    elif(n == 2):
        primo = True
    else:
        d = n % 2
        if(d == 0):
            primo = False
        x = 3
        while(x < n):
            d = n % x
            if(d == 0):
                primo = False
                break
            else:
                x += 2
    return primo

def imprime_primos(n):
    x = 0
    quantidade = 0
    while(quantidade < n):
        primo = verifica_primo(x)
        if(primo == True):
            print(x, end=" ")
            quantidade += 1
        x += 1

def main():
    cabecalho("Esse programa imprime os n primeiros primos.")

    n = verifica_int("Digite um número: ")

    imprime_primos(n)

main()
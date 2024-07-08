#Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a 0, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

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

def main():
    cabecalho("Esse programa verifica se um número é primo.")

    n = verifica_int("Digite um número: ")

    primo = verifica_primo(n)

    print("=" * 100)
    if(primo == True):
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")
    print("=" * 100)

main()
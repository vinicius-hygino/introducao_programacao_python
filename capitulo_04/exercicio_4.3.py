#Escreva um programa que leia três números e que imprima o maior e o menor.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número.")

def verifica_maior_menor(a, b, c):
    if(c > a) and (c > b):
        maior = c
        if(b > a):
            menor = a
        elif(a > b):
            menor = b
        else:
            menor = "O 1º e o 2º são iguais."
    elif(b > a) and (b > c):
        maior = b
        if(a > c):
            menor = c
        elif(c > a):
            menor = a
        else:
            menor = "O 1º e o 3º são iguais."
    elif(a > b) and (a > c):
        maior = a
        if(b > c):
            menor = c
        elif(c > b):
            menor = b
        else:
            menor = "O 2º e o 3º são iguais."
    else:
        maior = "Os números são iguais."
        menor = "Os números são iguais."
    return [maior, menor]
        

def main():
    cabecalho("Esse programa verifica o maior e o menor entre três números.")

    a = verifica_float("Digite o 1º número: ")
    b = verifica_float("Digite o 2º número: ")
    c = verifica_float("Digite o 3º número: ")

    maior_menor = verifica_maior_menor(a, b, c)

    print("=" * 100)
    print(f"Maior = {maior_menor[0]}")
    print(f"Menor = {maior_menor[1]}")
    print("=" * 100)

main()
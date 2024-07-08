#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utiliza apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4x5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

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

def multiplica(n1, n2):
    soma = 0
    if((n1 < 0) and (n2 > 0)) or ((n1 > 0) and (n2 < 0)):
        n1 = abs(n1)
        n2 = abs(n2)
        x = 0
        while(x < n2):
            soma += n1
            x += 1
        soma = soma * -1
    elif(n1 > 0) and (n2 > 0):
        x = 0
        while(x < n2):
            soma += n1
            x += 1
    else:
        n1 = abs(n1)
        n2 = abs(n2)
        x = 0
        while(x < n2):
            soma += n1
            x += 1
    return soma

def main():
    cabecalho("Esse programa multiplica dois números usando o operador de soma.")

    n1 = verifica_int("Digite o 1º número: ")

    n2 = verifica_int("Digite o 2º número: ")

    resultado = multiplica(n1, n2)

    print("=" * 100)
    print(f"{n1} x {n2} = {resultado}")
    print("=" * 100)

main()
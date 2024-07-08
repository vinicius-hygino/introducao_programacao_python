#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utiliza apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

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

def divide(n1, n2):
    if(n1 < 0) or (n2 < 0):
        n1 = abs(n1)
        n2 = abs(n2)
        x = 0
        while(n1 >= n2):
            n1 = n1 - n2
            x += 1
        return [-x, n1]
    elif(n1 < 0) and (n2 < 0):
        n1 = abs(n1)
        n2 = abs(n2)
        x = 0
        while(n1 >= n2):
            n1 = n1 - n2
            x += 1
        return [x, n1]
    elif(n2 == 0):
        return ["erro",0]
    else:
        x = 0
        while(n1 >= n2):
            n1 = n1 - n2
            x += 1
        return [x, n1]


def main():
    cabecalho("Esse programa divide dois números usando o operador de soma.")

    n1 = verifica_int("Digite o 1º número: ")

    n2 = verifica_int("Digite o 2º número: ")

    resultado = divide(n1, n2)

    print("=" * 100)
    print(f"{n1} / {n2} = {resultado[0]}")
    print(f"Resto = {resultado[1]}")
    print("=" * 100)

main()
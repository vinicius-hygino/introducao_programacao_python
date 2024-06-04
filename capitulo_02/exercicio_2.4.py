#Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def main():
    cabecalho("Esse programa mostra o resultado de uma multiplicação.")

    a = 3
    b = 5

    c = (2 * a) * (3 * b)

    print(f"O valor de 2a x 3b = {c}")

main()
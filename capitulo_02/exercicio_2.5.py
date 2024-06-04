#Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def main():
    cabecalho("Esse programa soma 3 variáveis.")

    a = 2
    b = 3
    c = 4

    d = a + b + c

    print(f"O valor da soma das três variáveis é de {d}")

main()
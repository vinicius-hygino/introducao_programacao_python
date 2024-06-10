#Escreva um programa que leia um valor em metros e o exiba convertido em milimetros.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número.")

def conversor(metros):
    milimetros = metros * 1000
    return milimetros

def main():
    cabecalho("Esse programa converte metros em milimetros.")

    metros = verifica_float("Digite o valor em metros: ")

    milimetros = conversor(metros)

    print("=" * 100)
    print(f"{metros} m = {milimetros} mm")
    print("=" * 100)

main()
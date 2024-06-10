#Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_inteiro(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("A entrada deve ser um número inteiro.")

def main():
    cabecalho("Esse programa soma dois números inteiros.")

    n1 = verifica_inteiro("Digite o primeiro número: ")
    n2 = verifica_inteiro("Digite o segundo número: ")

    soma = n1 + n2

    print("=" * 100)
    print(f"Resultado = {soma}")
    print("=" * 100)

main()
#Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²)

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser um número positivo")
        except Exception:
            print("A entrada deve ser um número.")

def area(lado):
    a = lado ** 2
    return a

def main():
    cabecalho("Esse programa calcula a área de um quadrado.")

    lado = verifica_float("Digite o valor do lado(cm): ")

    a = area(lado)

    print("-" * 100)
    print(f"A área é igual a {a} cm².")
    print("-" * 100)

main()
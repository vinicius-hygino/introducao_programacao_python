#Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2)

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um valor positivo.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_area(b,a):
    area = (b * a) / 2
    return area

def main():
    cabecalho("Esse programa calcula a área de um triângulo")

    base = verifica_float("Digite o valor da base(cm): ")
    altura = verifica_float("Digite o valor da altura(cm): ")

    area = calcula_area(base, altura)

    print("-" * 100)
    print(f"A área é de {area} cm²")
    print("-" * 100)

main()
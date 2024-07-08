#Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b = 2. Calcule p usando a fórmula p = (b + (n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

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
                print("A entrada deve ser um número maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_raiz(n):
    b = 2
    p = (b + (n/b)) / 2
    while True:
        if(abs(n - (p ** 2)) <= 0.0001):
            break
        b = p
        p = (b + (n/b)) / 2
    return p

def main():
    cabecalho("Esse programa calcula a raiz quadrada pelo método de Newton.")

    n = verifica_float("Digite um número para calcular a raiz quadrada: ")

    resultado = calcula_raiz(n)

    print("=" * 100)
    print(f"Resultado = {resultado}")
    print("=" * 100)

main()
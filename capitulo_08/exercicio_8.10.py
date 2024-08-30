#Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.
def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")

def fibonacci(n):
    lista = [1, 1, 2]
    x = 0
    a = 1
    b = 1
    c = 2
    while(x < (n - 3)):
        a = b
        b = c
        c = a + b
        lista.append(c)
        x += 1
    return lista[n - 1]

def main():
    cabecalho("Esse programa mostra um número da sequência de Fibonacci.")

    n = verifica_int("Digite o nº da sequência que você quer(ex= 10): ")

    resultado = fibonacci(n)

    print("=" * 100)
    print(f"O {n}º da sequência de Fibonacci é: {resultado}")
    print("=" * 100)

main()


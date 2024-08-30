#Defina uma função recursiva que calcule o maior divisor comum (MDC) entre dois números a e b, em que a > b.
def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_int_a(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número posivivo.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_int_b(pergunta, a):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 <= entrada < a):
                return entrada
            else:
                print("O valor de B deve ser menor que o valor de A e maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número.")

def mdc(a, b):
    if(b == 0):
        return a
    else:
        return mdc(b, (a % b))

def main():
    cabecalho("Esse programa calcula o MDC entre dois números, onde o valor de A deve ser maior que B.")

    a = verifica_int_a("Digite o valor de A: ")
    b = verifica_int_b("Digite o valor de B: ", a)

    resultado = mdc(a, b)

    print("-" * 100)
    print(f"MDC de {a} e {b} = {resultado}")
    print("-" * 100)

main()
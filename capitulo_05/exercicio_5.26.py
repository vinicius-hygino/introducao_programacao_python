#Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.

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
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_divisao(n1, n2):
    x = 0
    while(n1 >= n2):
        n1 = n1 - n2
        x += 1
    return [x , n1]

def main():
    cabecalho("Esse programa executa a divisão inteira entre dois números utilizando apenas soma e subtração.")

    n1 = verifica_float("Dividendo: ")
    n2 = verifica_float("Divisor: ")
    
    if(n2 == 0):
        print("Erro, o divisor não pode ser 0.")
    else:
        resultado = calcula_divisao(n1, n2)

        print("=" * 100)
        print(f"Resultado = {resultado[0]}")
        print(f"Resto = {resultado[1]}")
        print("=" * 100)

main()

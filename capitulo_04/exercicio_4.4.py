#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A entrada deve ser um número positivo.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_aumento(salario):
    if(salario > 1250):
        aumento = salario * 0.1
    else:
        aumento = salario * 0.15
    return aumento

def main():
    cabecalho("Esse programa calcula o aumento em um salário baseado no valor.")

    salario = verifica_float("Digite o valor do salário: ")

    aumento = calcula_aumento(salario)

    salario_final = salario + aumento

    print("=" * 100)
    print(f"Aumento = R$ {aumento}")
    print(f"Novo salário = R$ {salario_final}")
    print("=" * 100)

main()
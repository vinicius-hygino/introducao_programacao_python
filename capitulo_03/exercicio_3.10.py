#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salario e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

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
                print("O valor da entrada deve ser maior ou igual a 0")
        except Exception:
            print("O valor da entrada deve ser um número.")

def calcula_aumento(salario, taxa):
    salario_final = salario + (salario * (taxa / 100))
    return salario_final

def main():
    cabecalho("Esse programa calcula um aumento salarial.")

    salario = verifica_float("Digite o valor do salário(R$): ")
    taxa = verifica_float("Digite o valor da taxa de aumento(%): ")

    novo_salario = calcula_aumento(salario, taxa)

    print("=" * 100)
    print(f"Valor do aumento = R$ {(taxa / 100) * salario}")
    print(f"Novo salário: R$ {novo_salario}")
    print("=" * 100)

main()
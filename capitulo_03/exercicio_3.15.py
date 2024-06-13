#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_dias_perdidos(cigarros_dia, anos_fumando):
    min_dia = cigarros_dia * 10
    total_min = (min_dia * 364) * anos_fumando
    total_h = total_min / 60
    total_d = total_h / 24
    return total_d

def main():
    cabecalho("Esse programa calcula o tempo de vida perdidod por um fumante.")

    cigarros_dia = verifica_int("Digite o número de cigarros por dia: ")
    anos_fumando = verifica_int("Digite a quantidade de anos que já fumou: ")

    dias_perdidos = calcula_dias_perdidos(cigarros_dia, anos_fumando)

    print("=" * 100)
    print(f"Dias perdidos por conta do cigarro = {dias_perdidos:.0f}")
    print("=" * 100)

main()
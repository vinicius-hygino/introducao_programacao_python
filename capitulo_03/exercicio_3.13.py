#Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: f = ((9 * c) / 5) + 32

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            return entrada
        except Exception:
            print("O valor da entrada deve ser um número.")

def converte_c_f(temp_c):
    f = ((9 * temp_c) / 5) + 32
    return f

def main():
    cabecalho("Esse program converte uma temperatura em °C para °F")

    temp_c = verifica_float("Digite a temperatura em °C: ")

    temp_f = converte_c_f(temp_c)

    print("=" * 100)
    print(f"{temp_c} °C = {temp_f} °F")
    print("=" * 100)

main()

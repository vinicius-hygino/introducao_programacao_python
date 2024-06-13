#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

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
                print("O valor da entrada deve ser maior que 0.")
        except Exception:
            print("O valor da entrada deve ser um número.")

def calcula_preço(km, dias):
    preco = (dias * 60) + (0.15 * km)
    return preco

def main():
    cabecalho("Esse programa calcula o preço que um aluguel de carro irá custar.")

    km_percorridos = verifica_float("Digite a quantidade de Km percorridos: ")

    dias_alugados = verifica_float("Digite a quantidade de dias alugados: ")

    preco = calcula_preço(km_percorridos, dias_alugados)

    print("=" * 100)
    print(f"Preço a pagar = R$ {preco}")
    print("=" * 100)

main()

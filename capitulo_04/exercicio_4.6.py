#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.

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
                print("A entrada deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número.")

def calcula_preco(km):
    if(km <= 200):
        preco = km * 0.5
    else:
        preco = km * 0.45
    return preco

def main():
    cabecalho("Esse programa calcula o preço de uma viagem baseado no total de Km percorridos.")

    km = verifica_float("Digite a distância da viagem(Km): ")

    preco = calcula_preco(km)

    print("=" * 100)
    print(f"Preço = R$ {preco}")
    print("=" * 100)

main()

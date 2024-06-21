#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residência, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

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
                print("O valor da entrada deve ser igual ou maior que 0.")
        except Exception:
            print("O valor da entrada deve ser um número.")

def verifica_tipo(pergunta):
    lista = ["R", "r", "C", "c", "I", "i"]
    while True:
        entrada = input(pergunta)
        if(entrada in lista):
            entrada = entrada.upper()
            return entrada
        else:
            print("Caractere inválido, tente novamente.(R, I ou C)")

def calcula_preco(kwh, tipo):
    if(tipo == "R"):
        if(kwh <= 500):
            multiplicador = 0.4
        else:
            multiplicador = 0.65
    elif(tipo == "C"):
        if(kwh <= 1000):
            multiplicador = 0.55
        else:
            multiplicador = 0.6
    else:
        if(kwh <= 5000):
            multiplicador = 0.55
        else:
            multiplicador = 0.6
    preco = multiplicador * kwh
    return preco

def main():
    cabecalho("Esse programa calcula o preço da conta de energia elétrica baseando-se no tipo de edificação.")
    cabecalho("R-Residêncial, C-Comercial, I-Industrial")

    kwh = verifica_float("Digite o valor de kwh consumido: ")
    tipo = verifica_tipo("Digite o tipo de edificaçao: ")

    preco = calcula_preco(kwh, tipo)

    print("=" * 100)
    print(f"Preço = R$ {preco:.2f}")
    print("=" * 100)

main()
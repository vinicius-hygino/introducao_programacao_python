#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

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
                print("O valor da entrada deve ser positivo.")
        except Exception:
            print("A entrada deve ser um número.")

def exibe_valores(deposito, taxa):
    print("-" * 100)
    mes = 1
    valor = deposito
    total_juros = 0
    while(mes < 24):
        print(f"Mês {mes:<2} = R$ {valor:.2f}")
        juros = valor * (taxa / 100)
        valor = valor + juros
        total_juros += juros
        mes += 1
    print(f"Mês {mes:<2} = R$ {valor:.2f}")
    print("-" * 100)
    print(f"Total ganho com juros = R$ {total_juros:.2f}")
    print("-" * 100)

def main():
    cabecalho("Esse programa calcula o juros de uma poupança.")

    deposito = verifica_float("Digite o valor do depósito inicial(R$): ")
    taxa = verifica_float("Digite o valor da taxa de juros(%): ")

    exibe_valores(deposito, taxa)

main()
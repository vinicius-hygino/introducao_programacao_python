#Altere o program anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

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

def exibe_valores(deposito, taxa, valor_mensal):
    print("-" * 100)
    mes = 1
    valor = deposito
    total_juros = 0
    while(mes < 24):
        print(f"Mês {mes:<2} = R$ {valor:.2f}")
        juros = valor * (taxa / 100)
        valor = valor + juros + valor_mensal
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
    valor_mensal = verifica_float("Digite o valor depositado a cada mês: ")

    exibe_valores(deposito, taxa, valor_mensal)

main()
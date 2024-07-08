#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

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

def calcula_juros(valor_inicial, juros_mensal, pagamento_mensal):
    if(pagamento_mensal <= (valor_inicial * (juros_mensal / 100))):
        print("O valor do pagamento mensal é menor que a taxa de juros, a dívida só vai aumentar.")
    else:
        mes = 1
        total_juros = 0
        while(valor_inicial > 0):
            print(f"Mês {mes} | Dívida = R$ {valor_inicial:.2f} | Total de juros = R$ {total_juros:.2f}")
            juros = valor_inicial * (juros_mensal / 100)
            total_juros += juros
            valor_inicial = valor_inicial + juros - pagamento_mensal
            mes += 1

def main():
    cabecalho("Esse programa calcula o juros de uma dívida.")

    valor_inicial = verifica_float("Digite o valor da dívida: ")
    juros_mensal = verifica_float("Digite o juros mensal(%): ")
    pagamento_mensal = verifica_float("Digite o valor pago mensal: ")

    calcula_juros(valor_inicial, juros_mensal, pagamento_mensal)

main()
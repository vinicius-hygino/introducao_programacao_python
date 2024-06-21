#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

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
                print("O valor da entrada deve ser superior a 0.")
        except Exception:
            print("O valor da entrada deve ser um número.")

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor da entrada deve ser superior a 0.")
        except Exception:
            print("O valor da entrada deve ser um número inteiro.")

def calcula_prestacao(valor_casa, anos):
    meses = anos * 12
    prestacao = valor_casa / meses
    return prestacao

def verifica_prestacao(salario, prestacao):
    referencia = salario * 0.3
    if(prestacao <= referencia):
        return True
    else:
        return False

def main():
    cabecalho("Esse programa calcula as prestações de um financiamento sem juros.")

    valor_casa = verifica_float("Digite o valor do imóvel: ")

    salario = verifica_float("Digite a renda familiar: ")

    anos = verifica_int("Digite o número de anos que pretende pagar: ")

    prestacao = calcula_prestacao(valor_casa, anos)

    validade_prestacao = verifica_prestacao(salario, prestacao)

    print("-" * 100)
    if(validade_prestacao == False):
        print(f"Prestação = R$ {prestacao:.2f}")
        print("O valor da prestação excede o limite de 30% do salário, favor escolher pagar em mais tempo.")
    else:
        print(f"Prestação = R$ {prestacao:.2f}")
        print("Financiamento aprovado.")
    print("-" * 100)

main()
#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma(+), subtração(-), multiplicação(*) e divisão(/). Exiba  o resultado da operação solicitada.

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
            print("A entrada deve ser um número.")

def verifica_operacao(pergunta):
    lista_operadores = ["+", "-", "*", "/"]
    while True:
        entrada = input(pergunta)
        if(entrada in lista_operadores):
            return entrada
        else:
            print("Operador inválido, operadores suportados: +, -, *, /")

def calcula_resultado(n1, op, n2):
    if(op == "+"):
        resultado = n1 + n2
    elif(op == "-"):
        resultado = n1 - n2
    elif(op == "*"):
        resultado = n1 * n2
    else:
        resultado = n1 / n2
    return resultado

def main():
    cabecalho("Esse programa realiza quatro operações básicas entre dois números(+, -, *, /)")

    n1 = verifica_float("1º número: ")
    operacao = verifica_operacao("Operador: ")
    n2 = verifica_float("2º número: ")

    resultado = calcula_resultado(n1, operacao, n2)

    print("=" * 100)
    print(f"{n1} {operacao} {n2} = {resultado}")
    print("=" * 100)

main()
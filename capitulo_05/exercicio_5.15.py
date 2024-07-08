# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto.
# codigo  preço
# 1       0,50
# 2       1,00
# 3       4,00
# 5       7,00
# 9       8,00
#Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_codigo(pergunta):
    lista = [0,1,2,3,5,9]
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada in lista):
                return entrada
            else:
                print("Código inválido.")
        except Exception:
            print("O código deve ser um número inteiro.")

def verifica_quantidade(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("O valor da entrada deve ser maior ou igual a 0.")
        except Exception:
            print("O valor da entrada deve ser um número inteiro.")

def imprime_tabela():
    print("""  codigo    preço
#   1       0,50
#   2       1,00
#   3       4,00
#   5       7,00
#   9       8,00
#   0       Sai
""")

def consulta_valor(codigo):
    if(codigo == 1):
        valor = 0.5
    elif(codigo == 2):
        valor = 1
    elif(codigo == 3):
        valor = 4
    elif(codigo == 5):
        valor = 7
    else:
        valor = 8
    return valor

def main():
    cabecalho("Esse programa simula uma máquina registradora.")

    imprime_tabela()
    print("-" * 100)
    total = 0
    x = 1
    while True:
        codigo = verifica_codigo(f"Digite o código do {x}º produto: ")
        if(codigo == 0):
            break
        else:
            quantidade = verifica_quantidade("Digite a quantidade: ")
            valor_produto = consulta_valor(codigo)
            preco_compra = valor_produto * quantidade
            total += preco_compra
            x += 1
    
    print("=" * 100)
    print(f"Total das compras = R$ {total}")
    print("=" * 100)

main()
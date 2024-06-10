#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

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
                print("O valor da entrada deve ser maior que 0")
        except Exception:
            print("O valor da entrada deve ser um número.")

def calcula_desconto(preco, taxa):
    desconto = preco * (taxa / 100)
    return desconto

def calcula_novo_preco(preco, desconto):
    novo_preco = preco - desconto
    return novo_preco

def main():
    cabecalho("Esse programa calcula o desconto sobre o preço de uma mercadoria.")

    preco = verifica_float("Digite o valor da mercadoria: ")
    taxa = verifica_float("Digite o percentual de desconto(%): ")

    desconto = calcula_desconto(preco, taxa)
    novo_preco = calcula_novo_preco(preco, desconto)

    print("=" * 100)
    print(f"Valor do desconto = R$ {desconto}")
    print(f"Novo preço = R$ {novo_preco}")
    print("=" * 100)

main()
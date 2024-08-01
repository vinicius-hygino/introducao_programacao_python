#Altere o programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

#programa 6.22 - Exemplo de dicionário com estoque e operação de venda (modificado)
def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_produto(pergunta, estoque):
    while True:
        entrada = input(pergunta)
        if(entrada in estoque):
            return entrada
        else:
            print("Produto inválido.")

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("A quantidade deve ser maior que 0.")
        except Exception:
            print("A entrada deve ser um número inteiro.")
               
def imprime_estoque(estoque):
    print("Produto --- Preço")
    for chave, dados in estoque.items():
        print(f"{chave} --- {dados[1]}")

def main():
    cabecalho("Banca do seu João")
    
    estoque = {"tomate":[1000, 2.30], "alface":[500, 0.45], "batata":[2001, 1.20], "feijão":[100, 1.50]}

    imprime_estoque(estoque)

    venda = []
    while True:
        produto = verifica_produto("Digite o produto: ",estoque)
        quantidade = verifica_int("Digite a quantidade: ")

        venda.append([produto, quantidade])

        escolha = input("Deseja passar mais compras?(s/n): ")
        if(escolha == "n") or (escolha == "N"):
            break

    total = 0

    print("Vendas:\n")
    for operacao in venda:
        produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
        estoque[produto][0] -= quantidade
        total += custo

    print(f" Custo total: {total:21.2f}\n")

    print("Estoque: \n")
    for chave, dados in estoque.items():
        print("Descrição: ",chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")

main()
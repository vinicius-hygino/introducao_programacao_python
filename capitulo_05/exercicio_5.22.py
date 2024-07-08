# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

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
            print("Digite um número.")

def verifica_opcoes(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            if(0 <= entrada <= 4):
                return entrada
            else:
                print("Escolha uma opcão de 0 a 4.")
        except Exception:
            print("Entrada inválida.")

def imprime_menu():
    print("=" * 100)
    print("Selecione a operação desejada:")
    print("1-Adição\n2-Subtração\n3-Divisão\n4-Multiplicação\n0-Sair")
    print("=" * 100)

def imprime_tabuada(n, opcao):
    if(opcao == 1):
        x = 1
        while(x <= 10):
            print(f"{n} + {x} = {n + x}")
            x += 1
    elif(opcao == 2):
        x = 1
        while(x <= 10):
            print(f"{n} - {x} = {n - x}")
            x += 1
    elif(opcao == 3):
        x = 1
        while(x <= 10):
            print(f"{n} / {x} = {n / x}")
            x += 1
    elif(opcao == 4):
        x = 1
        while(x <= 10):
            print(f"{n} x {x} = {n * x}")
            x += 1

def main():
    cabecalho("Esse programa realiza a tabuada da operação selecionada.")

    while True:
        imprime_menu()
        opcao = verifica_opcoes("Escolha: ")
        if(opcao == 0):
            break
        else:
            n = verifica_float("Digite um número: ")
            print("-" * 100)
            imprime_tabuada(n, opcao)

main()


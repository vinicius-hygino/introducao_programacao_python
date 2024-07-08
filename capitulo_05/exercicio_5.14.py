#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0. No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritimética.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_int(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
            return entrada
        except Exception:
            print("O valor da entrada deve ser um número inteiro.")

def calcula_media(soma, x, lista):
    if(len(lista) != 0):
        media = soma / x
    else:
        media = 0
    return media

def main():
    cabecalho("Esse programa calcula a média e a soma de um conjunto de números.")
    print("Digite 0 para parar a execução.")
    
    lista = []
    soma = 0
    x = 0
    while True:
        n = verifica_int(f"Digite o {x + 1}º número: ")
        if(n == 0):
            break
        else:
            lista.append(n)
            soma += n
            x += 1
    
    media = calcula_media(soma, x, lista)

    print("=" * 100)
    print(f"Quantidade de números digitados: {x} | Soma: {soma} | Média: {media}")
    print("=" * 100)

main()
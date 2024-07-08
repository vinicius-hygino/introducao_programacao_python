#Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, 7, ..., 1, 0 e Fogo! na tela.

import time

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def contagem_regressiva(t):
    x = t
    while(x > 0):
        print(x)
        time.sleep(1)
        x -= 1
    print("Fogo!")

def main():
    cabecalho("Esse programa faz uma contagem regressiva de um foguete.")

    contagem_regressiva(10)

main()
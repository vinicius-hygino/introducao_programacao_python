#Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def imprime_multiplo_3(n):
    contador = 0
    while(contador < n):
        print(f"{contador} * 3 = {contador * 3}")
        contador += 1

def main():
    cabecalho("Esse programa imprime os 10 primeiros múltiplos de 3")

    imprime_multiplo_3(10)

main()
        


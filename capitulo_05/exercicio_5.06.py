#Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2X1 = 2, 2x2 = 4,...

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def imprime_multiplo_3(n):
    contador = 0
    while(contador < n):
        print(f"3x{contador} = {contador * 3}")
        contador += 1

def main():
    cabecalho("Esse programa imprime os 10 primeiros múltiplos de 3")

    imprime_multiplo_3(10)

main()
        
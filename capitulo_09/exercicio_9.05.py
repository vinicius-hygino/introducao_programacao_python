#Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deve conter o maior número; e a última, o menor.

with open("pares.txt","r") as pares:
    lista_pares = []
    for e in pares.readlines():
        lista_pares.append(int(e))
    print(lista_pares[-500])

pares_invertido = []
x = -1
while(x >= len(lista_pares) * -1):
    pares_invertido.append(lista_pares[x])
    x -= 1

with open("paresinvertidos.txt", "w") as paresinvertidos:
    for e in pares_invertido:
        paresinvertidos.write(f"{e}\n")

    
    
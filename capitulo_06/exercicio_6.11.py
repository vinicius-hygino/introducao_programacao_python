#Modifique o programa 6.6 usando o for. Explique por que nem todos os while podem ser transformados em for.

#programa 6.6 - Adição de elementos à lista (modificado)
L = []
while True: #esse while não pode ser substituido por for sem alterar a essência do programa
    n = int(input("Digite um número (0 sai): "))
    if(n == 0):
        break
    L.append(n)

for e in L: #Aqui havia um while para mostrar a lista.
    print(e)
    
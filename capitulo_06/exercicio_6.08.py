#Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.

#Programa 6.9 - Pesquisa sequêncial (modificado)
l = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0
while(x < len(l)):
    if(l[x] == p):
        print(f"{p} encontrado na posição {x}")
        break
    x += 1

if(x >= len(l)):
    print(f"{p} não encontrado.")
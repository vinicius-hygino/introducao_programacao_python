#Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.

#Programa 6.9 - Pesquisa sequêncial (modificado)
l = [15, 7, 27, 39]
p = int(input("Digite o 1º valor a procurar: "))
v = int(input("Digite o 2º valor a procurar: "))
if(p == v):
    print("Os dois valores são iguais. Tente novamente.")
else:
    x = 0
    achou_p = False
    achou_v = False
    while(x < len(l)):
        if(l[x] == p):
            achou_p = True
            posicao_p = x
        elif(l[x] == v):
            achou_v = True
            posicao_v = x
        x += 1

    print("=" * 100)
    if(achou_p == True) and (achou_v == True):
        print(f"{p} encontrado na posição {posicao_p}")
        print(f"{v} encontrado na posição {posicao_v}")
        if(posicao_p > posicao_v):
            print(f"{v} foi encontrado primeiro.")
        elif(posicao_p < posicao_v):
            print(f"{p} foi encontrado primeiro.")
        else:
            print("Os dois valores são iguais.")
    elif(achou_p == True) and (achou_v == False):
        print(f"{p} encontrado na posição {posicao_p}")
        print(f"{v} não foi encontrado.")
    elif(achou_p == False) and (achou_v == True):
        print(f"{v} encontrado na posição {posicao_v}")
        print(f"{p} não foi encontrado.")
    else:
        print("Nenhum dos valores foi encontrado!")
    print("=" * 100)

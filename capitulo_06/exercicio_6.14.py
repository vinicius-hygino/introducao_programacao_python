#O que acontece quando a lista já está ordenada? Rastreie o programa 6.20, mas com a lista L=[1,2,3,4,5]

#Programa 6.20
l = [1,2,3,4,5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1): #roda todos os elementos da lista 
        if l[x] > l[x + 1]: #Se o anterior é maior que o posterior
            trocou = True
            temp = l[x]
            l[x] = l[x + 1] #troca
            l[x + 1] = temp #troca
        x += 1
    if not trocou: #se não mudou nenhum elemento, encerra a execução. Para uma lista em ordem o primeiro while roda uma única vez.
        break
    fim -= 1
for e in l:
    print(e)
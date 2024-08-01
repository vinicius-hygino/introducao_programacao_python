#Modifique o Programa 6.20 para ordenar a lista em ordem decrescente. L = [1,2,3,4,5] deve ser ordenada como L = [5,4,3,2,1].

#Programa 6.20
l = [1,2,3,4,5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1): #roda todos os elementos da lista 
        if l[x] < l[x + 1]: #Se o antual é menor que o posterior, troca
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

#foi necessário mudar apenas o sinal ">" por "<" para inverter a função do algorítimo.
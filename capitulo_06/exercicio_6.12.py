#Altere o programa 6.11 de forma a imprimir o menor elemento da lista

#programa 6.11 - Verificação do maior valor (modificado)
l = [1, 7, 2, 4]
minimo = l[0] #variavel alterada
for e in l:
    if(e < minimo):
        minimo = e
print(minimo)
#Escreva uma função que retorne o maior de dois números.
#Valores esperados:
#maximo(5,6) == 6
#maximo(2,1) == 2
#maximo(7,7) == 7

def maximo(n1, n2):
    if(n1 > n2):
        return n1
    elif(n1 < n2):
        return n2
    else:
        return n1

print(maximo(5,6))
print(maximo(2,1))
print(maximo(7,7))
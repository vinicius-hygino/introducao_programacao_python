#Escreva um generator capaz de gerar a sequência dos números primos.

def gerador_de_primos():
    i = 2
    while True:
        x = 1
        d = 0
        while(x <= i):
            if(i % x == 0):
                d += 1
            x += 1
        if(d == 2):
            yield i
        i += 1

g = gerador_de_primos()

for e in range(11):
    print(next(g))
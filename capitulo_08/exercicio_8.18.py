#Escreva um generator capaz de gerar a sequência de Fibanacci.

def gerador_fibonacci():
    a = 1
    yield a
    b = 1
    c = 2
    while True:
        yield b
        a = b
        b = c
        c = a + b



g = gerador_fibonacci()

for e in range(11):
    print(next(g))
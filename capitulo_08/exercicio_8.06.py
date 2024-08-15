#Reescreva o Programa 8.2 de forma a utilizar for em vez de while

#Programa 8.2 - Como não escrever uma função
# def soma(L):
#     total = 0
#     x = 0
#     while x < 5:
#         total += L[x]
#         x += 1
#     return total

def soma(L):
    total = 0
    for e in L:
        total += e
    return total

L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4])) # não funciona na primeira execução porque só soma os 5 primeiros elementos devido a linha 7


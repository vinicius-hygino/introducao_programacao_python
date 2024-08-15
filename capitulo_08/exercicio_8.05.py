#Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no capítulo 07.

#Porgrama 8.1 - Pesquisa em um lista
# def pesquise(lista, valor):
#     for x, e in enumerate(lista):
#         if e == valor:
#             return x
#     return None

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
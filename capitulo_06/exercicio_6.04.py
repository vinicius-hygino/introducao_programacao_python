#O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?

lista = [1, 2, 3, 4, 5]
print(lista)
lista.pop(0)
print(lista)
lista.pop(0)
print(lista)
lista.pop(0)
print(lista)
lista.pop(0)
print(lista)
lista.pop(0)
print(lista)
lista.pop(0)
print(lista)

#Ocorre um indexerror: pop from empty list, porém ele executa até a linha onde tentamos retirar da lista vazia.
#A lista de temperaturas de Mons, na Belgica, foi armazenada na lista T=[-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def menor_valor(lista):
    menor = lista[0]
    for e in lista:
        if(e < menor):
            menor = e
    return menor

def maior_valor(lista):
    maior = lista[0]
    for e in lista:
        if(e > maior):
            maior = e
    return maior

def calcula_media(lista):
    soma = 0
    for e in lista:
        soma += e
    media = soma / len(lista)
    return media

def main():
    cabecalho("Esse programa mostra informações sobre uma lista")
    lista = [-10, -8, 0, 1, 2, 5, -2, -4]
    print(f"Lista: {lista}")
    maior = maior_valor(lista)
    menor = menor_valor(lista)
    media = calcula_media(lista)

    print("=" * 100)
    print(f"Maior temperatura: {maior} °C")
    print(f"Menor temperatura: {menor} °C")
    print(f"Media das temperaturas {media} °C")
    print("=" * 100)

main()

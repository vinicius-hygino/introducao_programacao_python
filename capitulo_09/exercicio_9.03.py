#Crie um programa que leia os arquivos pares.txt e impares.txt e que crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica

with open("impares.txt","r") as impares:
    with open("pares.txt", "r") as pares:
        lista_pares = []
        for l in pares.readlines():
            lista_pares.append(int(l))
        
        lista_impares = []
        for l in impares.readlines():
            lista_impares.append(int(l))

with open("pareseimpares.txt", "w") as pareseimpares:
    lista_pareseimpares = []
    x = 0
    while(x < 500):
        lista_pareseimpares.append(lista_pares[x])
        lista_pareseimpares.append(lista_impares[x])
        x += 1
    
    for l in lista_pareseimpares:
        pareseimpares.write(f"{l}\n")

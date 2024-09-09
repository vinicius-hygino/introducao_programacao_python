#Modifique o programa do exercício 9.7 para também receber o número de caracteres por linha e o número de linhas por página pela linha de comando.

import sys

with open("lorenipsilon.txt") as arquivo:
    texto = []
    for l in arquivo.readlines():
        texto.append(l.split( ))
    
    palavras = []
    for linhas in texto:
        for p in linhas:
            palavras.append(p)

with open("lorenipsilonpaginado.txt", "w") as arquivopaginado:
    n_linhas_por_pagina = sys.argv[2]
    largura = sys.argv[1]

    paginas = 1
    linhas = 0
    contador = 0
    for e in palavras:
        if(contador > int(largura)):
            arquivopaginado.write("\n")
            contador = 0
            linhas += 1
        elif(linhas >= int(n_linhas_por_pagina)):
            arquivopaginado.write("\n")
            arquivopaginado.write(f"Loren Ipsilon {paginas}".rjust(int(largura)))
            arquivopaginado.write("\n")
            arquivopaginado.write("\n")
            linhas = 0
            paginas += 1
        else:
            arquivopaginado.write(f"{e} ")
            contador += (len(e) + 1)
    
    arquivopaginado.write("\n")
    arquivopaginado.write(f"Loren Ipsilon {paginas}".rjust(int(largura)))
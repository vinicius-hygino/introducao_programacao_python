#Crie um arquivo que leia um arquivo-texto e gere um arquivo de saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas. Adicione na última linha de cada página o número da página atual e o nome do arquivo original.

with open("lorenipsilon.txt") as arquivo:
    texto = []
    for l in arquivo.readlines():
        texto.append(l.split( ))
    
    palavras = []
    for linhas in texto:
        for p in linhas:
            palavras.append(p)

with open("lorenipsilonpaginado.txt", "w") as arquivopaginado:
    paginas = 1
    linhas = 0
    largura = 76
    contador = 0
    for e in palavras:
        if(contador > largura):
            arquivopaginado.write("\n")
            contador = 0
            linhas += 1
        elif(linhas >= 60):
            arquivopaginado.write("\n")
            arquivopaginado.write(f"Loren Ipsilon {paginas}".rjust(largura))
            arquivopaginado.write("\n")
            arquivopaginado.write("\n")
            linhas = 0
            paginas += 1
        else:
            arquivopaginado.write(f"{e} ")
            contador += (len(e) + 1)
    
    arquivopaginado.write("\n")
    arquivopaginado.write(f"Loren Ipsilon {paginas}".rjust(largura))
    
    


    
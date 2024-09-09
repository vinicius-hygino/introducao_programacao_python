#Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere um arquivo de saída com as linhas do primeiro e do segundo.

import sys
with open("terceiroarquivo.txt", "w") as arquivo3:
    with open(sys.argv[1], "r") as arquivo1:
        with open(sys.argv[2], "r") as arquivo2:
            data1 = arquivo1.readlines()
            data2 = arquivo2.readlines()
        for l in data1:
            arquivo3.write(f"{l}\n")
        for l in data2:
            arquivo3.write(f"{l}\n")
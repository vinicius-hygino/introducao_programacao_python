#Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo

import sys
#Esse bloco imprime o número de parâmetros, no caso desse programa 2: [nome do arquivo py, nome do arquivo txt]
print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")

#Esse bloco resolve o exercício, note que o nome do arquivo a ser lido é o sys.argv[1] pois o sys.argv[0] é exercicio_9.01.py
#A execução no cmd deve ser "python exercicio_9.01.py numeros.txt"
nome = sys.argv[1]
with open(nome, "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
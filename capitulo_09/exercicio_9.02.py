#Modifique o programa do Exercício 9.1 para que recaba mais dois parâmetros: a linha de início e de fim para impressão. O programa deve imprimir apenas as linhas entre esses dois valores(incluindo as linhas de inicio e fim)

import sys
#Esse bloco imprime o número de parâmetros, no caso desse programa 2: [nome do arquivo py, nome do arquivo txt]
print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")
print("\n")

#Esse bloco resolve o exercício, note que o nome do arquivo a ser lido é o sys.argv[1] pois o sys.argv[0] é exercicio_9.01.py
#A execução no cmd deve ser "python exercicio_9.01.py numeros.txt"

if(len(sys.argv) <= 2):
    print("Digite as linhas que deseja imprimir como parâmetros(nome inicio fim)")
else:
    try:
        nome = sys.argv[1]
        inicio = sys.argv[2]
        fim = sys.argv[3]
        n_linha = 0
        with open(nome, "r") as arquivo:
            for linha in arquivo.readlines():
                if(n_linha >= int(inicio)) and (n_linha <= int(fim)):
                    print(linha)
                n_linha += 1
    except IndexError:
        print("Deve-se digitar dois parâmetros de número de páginas.")
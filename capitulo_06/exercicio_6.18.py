#Escreva um programa que gere um dicionario, em que cada chave seja um caractere, e seu valor seja o número desse caractere encontrado um uma frase lida. Exemplo: O rato -> {"O":1, "r":1, "a":1,"t":1,"o":1}

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_entrada(pergunta):
    lista = []
    entrada = input(pergunta)
    for e in entrada:
        if(e != " "):
            lista.append(e)
    return lista

def main():
    cabecalho("Esse programa gera um dicionário.")

    frase = verifica_entrada("Digite uma frase: ")

    dicionario = {}
    for e in frase: #percorre cada letra
        contador = 0
        for i in frase: #percorre cada letra para comparar com a letra da vez
            if(e == i): #encontrando letras iguais aumenta a contagem
                contador += 1
        dicionario[e] = contador #crias as chaves e relaciona o numero como os dados
    
    print(dicionario)


main()
#Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
#string: TTAAC
#Resultado: T:2x A:2x C:1x

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa conta quantas vezes cada caractere aparece.")

    string = input("Digite uma palavra: ")

    dicionario = {}
    
    for e in string: #percorre todas as letras
        contador = 0
        for i in string:
            if(e == i): #compara cada letra com cada uma das letras
                contador += 1 #se forem iguais aumenta o contador
        dicionario[e] = contador #Adiciona chaves "e" no dicionario atribuindo o contador a cada uma
    
    for chave, dados in dicionario.items():
        print(f"{chave}: {dados}x")

main()
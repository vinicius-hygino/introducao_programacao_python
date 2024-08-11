#Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
#1ª string: AABBEFAATT
#2ª string: BE
#Resultado: BE encontrado na posição 3 de AABBEFAATT

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa verifica se uma string está contida em outra")

    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    print("=" * 100)
    if(string2 in string1):
        print("A string 2 está contida na string 1")
        
        posicao = 0
        while(posicao > -1): #o médoto find retorna -1 quando não encontra 
            posicao = string1.find(f"{string2}", posicao) #esse argumento informa para o algorítimo começar a procurar pela posição informada após a virgula
            if(posicao >= 0):
                print(f"Posição {posicao}")
                posicao += 1 #incrementamos a posicao a cada laço para não achar a mesma ocorrência novamente
    else:
        print("A segunda string não está contida na primeira.")
    print("=" * 100)

main()
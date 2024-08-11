#Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
#1ª string: AAACTBF
#2ª string: CBT
#3ª string: CBT
#A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa acha as letras comuns em duas palavras.")

    string1 = input("Digite uma palavra: ")
    string2 = input("Digite outra palavra: ")

    c1 = set(string1)
    c2 = set(string2)

    resultado = c1 & c2
    
    r = "".join(resultado)
    
    print("-" * 100)
    if(r == ""):
        print("Não há caracteres em comum.")
    else:
        print(f"Caracteres em comum: {r}")
    print("-" * 100)

main()
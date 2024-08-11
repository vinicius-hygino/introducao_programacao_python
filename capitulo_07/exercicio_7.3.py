#Escreva um programa que leia duas strings e gere uma tereceira apenas com os caracteres que aparecem em uma delas
#1ª string: CTA
#2ª string: ABC
#3ª string: BT
#A ordem dos caracteres da terceira string não é importante

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def main():
    cabecalho("Esse programa mostra os caracteres únicos em cada palavra digitada.")

    string1 = input("Digite a primeira palavra: ")
    string2 = input("Digite a segunda palavra: ")

    r = []
    for e in string1:
        if(e in string1) and (e not in string2):
            r.append(e)
    
    for i in string2:
        if(i in string2) and (i not in string1):
            r.append(i)
    
    resultado = "".join(r)

    print("-" * 100)
    if(resultado == ""):
        print("Não há caracteres únicos nas duas palavras")
    else:
        print(f"Resultado: {resultado}")
    print("-" * 100)

main()
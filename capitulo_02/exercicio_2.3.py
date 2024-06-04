#Faça um programa que exiba seu nome na tela

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def main():
    cabecalho("Esse programa exibe meu nome na tela.")

    print("Vinícius Gomes Hygino Silva.")

main()
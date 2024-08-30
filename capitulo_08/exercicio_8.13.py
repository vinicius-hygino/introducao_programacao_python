#Escreva uma função que receba uma string com as opções válidas a aceitar(cada opção é uma letra). Converta as opções válidas para letras minúsculas. Utilize input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção é válida. Em caso de opção inválida, a função deve pedir ao usuário que digite novamente outra opção.

def cabecalho(titulo):
    print("=" * 100)
    print(f"{titulo:^100}")
    print("=" * 100)

def verifica_opcao(string):
    string = string.lower()
    while True:
        opcao = input("Digite a opção: ").lower()
        if(opcao in string):
            return opcao
        else:
            print("Opção inválida, digite outra opção.")

def main():
    cabecalho("Esse programa exemplifica o uso de uma função verificadora de entrada.")

    print("Assinale a alternativa que corresponde ao valor de x, sendo x um número natural e x² + 2 = 11:")
    print("""
a) 3
b) 4
c) 2
d) 9
e) 1""")

    resposta = verifica_opcao("abcde")

    print("-" * 100)
    if(resposta == "a"):
        print("Resposta correta!")
    else:
        print("Resposta incorreta!")
    print("-" * 100)

main()
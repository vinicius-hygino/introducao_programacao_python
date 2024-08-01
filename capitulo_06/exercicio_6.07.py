#Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:
#(())   ok
#()()(()()) ok
#()) Erro

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_entrada(pergunta):
    lista = [")", "("]
    while True:
        entrada = input(pergunta)
        for e in entrada:
            if(e in lista):
                correto = True
            else:
                correto = False
        if(correto == True):
            return entrada
        else:
            print("Entrada incorreta, digite uma sequência de parenteses.")

def verifica_sequencia(entrada):
    pilha = []
    for e in entrada:
        if(e == "("):
            pilha.append("(")
        else:
            try:
                pilha.pop(-1)
            except Exception:
                return False
    x = 0
    for e in pilha:
        x += 1
    if(x == 0):
        return True
    else:
        return False

def main():
    cabecalho("Esse programa verifica uma sequência de parênteses.")

    entrada = verifica_entrada("Digite a sequência de parênteses: ")
    
    resultado = verifica_sequencia(entrada)

    print("=" * 100)
    if(resultado == True):
        print("Correto!")
    else:
        print("Errado!")
    print("=" * 100)

main()
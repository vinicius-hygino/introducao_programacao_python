#Reescreva o programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utiliza repetições aninhadas.

#programa 5.1 - Contagem de cédulas(modificado)

while True:
    valor = float(input("Digite o valor a pagar: "))
    if(valor == 0):
        print("Fim da execução!")
        break
    cédulas = 0
    atual = 100
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            if(atual % 1 == 0):
                print(f"{cédulas} cédula(s) de R$ {atual}")
            else:
                print(f"{cédulas} moeda(s) de R$ {atual}")
            if apagar < 0.01:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.5
            elif atual == 0.5:
                atual = 0.25
            elif atual == 0.25:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.01
            cédulas = 0
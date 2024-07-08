#O que acontece se digitarmos 0.001 no programa anterior? caso ele não funcione, altere-o de forma a corrigir o problema.

#programa 5.1 - Contagem de cédulas(modificado)
valor = float(input("Digite o valor a pagar: "))
cédulas = 0
atual = 50
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
        if atual == 50:
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

#Ao digitar 0.001 o programa entra em loop infinito, pois o programa passa por todas as linhas mas o valor apagar é menor que o menor atual. Com isso torna-se impossível pagar o valor. Uma possível solução é alterar a linha 17 para dar break se o valor de apagar for menor que 0.01(menor valor em moeda possível)
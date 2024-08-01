# Altere o programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.
#Exemplo: FFFAAAS significa três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa.

#Programa 6.7 - Simulação de uma fila de banco (modificado)
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    entrada = input("Operação (F, A ou S): ")
    x = 0
    while x < len(entrada): #adicionei outro laço, se não impor limite ocorre indexerro pois o x cresce até encontrar um S.
        operacao = entrada[x] #percorre cada elemento da entrada
        if operacao == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
    if operacao == "S": #O S precisa sair dos dois laços
        break
    
   
#Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G para fila 2

#Programa 6.7 - Simulação de uma fila de banco (modificado)
ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"Existem {len(fila2)} clientes na fila 2")
    print("\n")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("\n")
    print("F adiciona cliente na fila 1.")
    print("G adiciona cliente na fila 2.")
    print("A atendimento fila 1.")
    print("B atendimento fila 2.")
    print("S sai.")
    entrada = input("Operação (F, G, A, B ou S): ")
    x = 0
    while x < len(entrada): #adicionei outro laço, se não impor limite ocorre indexerro pois o x cresce até encontrar um S.
        operacao = entrada[x] #percorre cada elemento da entrada
        if operacao == "A":
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)
                print(f"Cliente {atendido1} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "B":
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)
                print(f"Cliente {atendido1} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ultimo1 += 1
            fila1.append(ultimo1)
        elif operacao == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
    if operacao == "S": #O S precisa sair dos dois laços
        break
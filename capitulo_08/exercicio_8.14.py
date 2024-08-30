#Altere o programa 8.20 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes.

#Programa 8.20
import random
n = random.randint(1, 10)
erros = 0
while(erros < 3):
    x = int(input("Escolha um número entre 1 e 10: "))
    if x == n:
        print("Você acertou!")
        break
    else:
        print("Você errou!")
        erros += 1

print("-" * 100)
print("Fim de jogo.")
if(erros == 3):
    print(f"O número secreto era {n}")
print("-" * 100)
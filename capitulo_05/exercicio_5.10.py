#Modifique o programa anterior para que aceite respostas com letras maíusculas e minúsculas em todas as questões.

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ").lower() #foi adicionado a função lower() apenas.
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao = questao + 1
print(f"O aluno fez {pontos} ponto(s)")
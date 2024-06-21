#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada >= 0):
                return entrada
            else:
                print("A entrada deve ser maior ou igual a 0.")
        except Exception:
            print("A entrada deve ser um número.")

def verifica_velocidade(v):
    if(v > 80):
        multa = (v - 80) * 5
        print("Você foi multado!")
        print(f"Valor da multa R$ {multa}")
    else:
        print("Parabéns por dirigir dentro do limite da via.")

def main():
    cabecalho("Esse programa verifica a velocidade de um carro e aplica multa se necessário.")
    cabecalho("Limite de velocidade da via = 80 km/h")
    velocidade = verifica_float("Digite a velocidade atual(km/h): ")

    verifica_velocidade(velocidade)

main()
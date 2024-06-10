#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

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
                print("O valor da entrada deve ser maior ou igual a 0")
        except Exception:
            print("O valor da entrada deve ser um número.")

def converte_tempo_em_segundo(d, h, m, s):
    horas = (d * 24) + h
    segundos = (horas * 3600) + (m * 60) + s
    return segundos
    

def main():
    cabecalho("Esse programa converte dias, horas e minutos em segundos.")

    dias = verifica_float("Digite a quantidade de dias: ")
    horas = verifica_float("Digite a quantidade de horas: ")
    minutos = verifica_float("Digite a quantidade de minutos: ")
    segundos = verifica_float("Digite a quantidade de segundos: ")

    s = converte_tempo_em_segundo(dias, horas, minutos, segundos)

    print("=" * 100)
    print(f"Número de segundos: {s} s")
    print("=" * 100)

main()
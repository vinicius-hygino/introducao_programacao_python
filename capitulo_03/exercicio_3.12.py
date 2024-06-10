#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

def cabecalho(titulo):
    print("-" * 100)
    print(f"{titulo:^100}")
    print("-" * 100)

def verifica_float(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
            if(entrada > 0):
                return entrada
            else:
                print("O valor da entrada deve ser maior que 0")
        except Exception:
            print("O valor da entrada deve ser um número.")

def calcula_tempo(d, v):
    t = d / v
    return t

def converte_tempo(t):
    h = t // 1
    sobra_h = t % 1
    min = (sobra_h * 60) // 1
    sobra_m = (sobra_h * 60) % 1
    s = sobra_m * 60
    return [h, min, s]

def main():
    cabecalho("Esse programa calcula o tempo de uma viagem de carro.")

    distancia = verifica_float("Digite a distância a percorrer(Km): ")
    velocidade = verifica_float("Digite a velocidade média esperada(km/h): ")

    tempo = calcula_tempo(distancia, velocidade)

    tempo_convertido = converte_tempo(tempo)
    
    print("=" * 100)
    print(f"Tempo aproximado = {tempo_convertido[0]:.0f} h, {tempo_convertido[1]:.0f} min, {tempo_convertido[2]:.0f} s")
    print("=" * 100)

main()
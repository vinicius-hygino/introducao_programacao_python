#Execute o programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do programa 4.2

#programa 4.4 - Carro novo ou velho, dependendo da idade com else
idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else: #O programa 4.2 usa 'if idade > 3' ao inves de else. Os dois programas obtêm o mesmo resultado.
    print("Seu carro é velho")
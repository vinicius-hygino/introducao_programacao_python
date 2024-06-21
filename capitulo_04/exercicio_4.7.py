#Rastreie o Programa 4.6. Compare seu resultado ao apresentado na tabela 4.2

#Programa 4.6 - Categoria x preço
categoria = int(input("Digite a categoria do produto: "))
if(categoria == 1):
    preco = 10
else:
    if(categoria == 2):
        preco = 18
    else:
        if(categoria == 3):
            preco = 23
        else:
            if(categoria == 4):
                preco = 26
            else:
                if(categoria == 5):
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
print(f"O preço do produto é: R${preco:6.2f}")

#Rastreio
#categoria    preco
#    1         10
#    2         18
#    3         23
#    4         26
#    5         31
#    6         0
#Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso contrário.

def tamanho_string(string, min, max):
    if(min <= len(string) <= max):
        return True
    else:
        return False

print(tamanho_string("vinicius", 3, 10))
print(tamanho_string("oi", 3, 10 ))
print(tamanho_string("paralelepípedo", 3, 10))
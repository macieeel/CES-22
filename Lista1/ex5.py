import math   # biblioteca para operações matemáticas

def is_palindrome(n):   # checa se uma string n é palíndromo

    size = len(n)   # variável contento o comprimento da string
    n_lower = n.lower()   # deixa tudo minúsculo para não haver distinção entre maiúsculas e minúsculas

    for i in range(math.floor(size / 2)):   # percorre a string do primeiro elemento até a metade
        if n_lower[i] != n_lower[size-1-i]:
            return False   # se quaisquer dois elementos em posições simétricas forem diferentes retorna falso

    return True   # se todos em posições simétricas forem iguais retorna verdadeiro

string = input("Digite uma palavra: ")   # recebe entrada do usuário

if is_palindrome(string):   # chama a função e printa se a palavra é um palíndromo ou não
    print(string, "é palíndromo")
else:
    print(string, "não é palíndromo")
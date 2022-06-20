import math   # biblioteca para operações matemáticas

def is_prime(n):   # checa se um número n é primo

    for i in range(2, math.floor(math.sqrt(n) + 1)):   # for de 2 até a raíz do número
        if (n % i == 0): 
            return False   # se for múltiplo de algum desses números retorna falso

    return True   # caso contrário retorna verdadeiro

n = 49   # define um número n
print(is_prime(n))   # printa o reultado da função
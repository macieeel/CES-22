def sum_to(n):   # faz a soma de 1 a n
    
    sum = 0
    for i in range(n+1):   # realiza a soma de todos os números de 1 a n
        sum += i
    
    return sum   # retorna a soma

n = 11   # define um número n
print(sum_to(n))   # printa o reultado da função
def decorator_sum_elements(function):
    def wrapper(*args, **kwargs):
        # decorador que soma os elementos passados para a funcao
        sum = 0
        for num in args:
            sum += num
        for num in kwargs.values():
            sum += num
        function(*args, **kwargs)
        print(f'A soma desses números é {sum}\n')
    return wrapper


@decorator_sum_elements
# função que printa os numeros passados
def my_function(*args, **kwargs):
    for index, num in enumerate(args, start=1):
        print(f'num{index} = {num}')

    for key, value in kwargs.items():
        print(f'{key} = {value}')


# usando somente lista como argumento
my_function(1, 2, 3)

# usando chaves e valores como argumento
my_function(a=1, b=2, c=3)

# usando lista e chaves e valores como argumento
my_function(1, 2, 3, a=4, b=5)

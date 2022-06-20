from abc import ABC


class BoloChocolate(ABC):
    def __init__(self):
        print("\nBolo de Chocolate")


class BoloMandioca(ABC):
    def __init__(self):
        print("\nBolo de Mandioca")


class BoloCenoura(ABC):
    def __init__(self):
        print("\nBolo de Cenoura")

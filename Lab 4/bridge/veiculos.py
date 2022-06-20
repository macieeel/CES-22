
from abc import ABC


class VeiculoAbstrato(ABC):
    def __init__(self, motor):
        pass


class Carro(VeiculoAbstrato):
    def __init__(self, motor):
        super().__init__(motor)
        print("Carro\n")


class Caminhao(VeiculoAbstrato):
    def __init__(self, motor):
        super().__init__(motor)
        print("Caminhão\n")


class Moto(VeiculoAbstrato):
    def __init__(self, motor):
        super().__init__(motor)
        print("Moto\n")

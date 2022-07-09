
from abc import ABC


class VeiculoAbstrato(ABC):
    def __init__(self, motor):
        self.motor = motor


class Carro(VeiculoAbstrato):
    # Atributos do carro
    def __init__(self, motor):
        super().__init__(motor)
        print("Carro\n")


class Caminhao(VeiculoAbstrato):
    # Atributos do caminhão
    def __init__(self, motor):
        super().__init__(motor)
        print("Caminhão\n")


class Moto(VeiculoAbstrato):
    # Atributos da moto
    def __init__(self, motor):
        super().__init__(motor)
        print("Moto\n")

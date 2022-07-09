from abc import ABC, abstractmethod
from motores import MotorCombustao, MotorEletrico, MotorHibrido
from veiculos import Carro, Caminhao, Moto


class FabricaAbstrata(ABC):
    # Fabrica abstrata de veiculos
    @abstractmethod
    def motorEletrico(self):
        pass

    @abstractmethod
    def motorCombustao(self):
        pass

    @abstractmethod
    def motorHibrido(self):
        pass


class FabricaCarro(FabricaAbstrata):
    # Fabrica concreta de carros
    def motorEletrico(self):
        super().motorEletrico()
        motor = MotorEletrico()
        Carro(motor)

    def motorCombustao(self):
        super().motorCombustao()
        motor = MotorCombustao()
        Carro(motor)

    def motorHibrido(self):
        super().motorHibrido()
        motor = MotorHibrido
        Carro(motor)


class FabricaMoto(FabricaAbstrata):
    # Fabrica concreta motos
    def motorEletrico(self):
        super().motorEletrico()
        motor = MotorEletrico()
        Moto(motor)

    def motorCombustao(self):
        super().motorCombustao()
        motor = MotorCombustao()
        Moto(motor)

    def motorHibrido(self):
        super().motorHibrido()
        motor = MotorHibrido
        Moto(motor)


class FabricaCaminhao(FabricaAbstrata):
    # Fabrica concreta de caminhoes
    def motorEletrico(self):
        super().motorEletrico()
        motor = MotorEletrico()
        Caminhao(motor)

    def motorCombustao(self):
        super().motorCombustao()
        motor = MotorCombustao()
        Caminhao(motor)

    def motorHibrido(self):
        super().motorHibrido()
        motor = MotorHibrido
        Caminhao(motor)

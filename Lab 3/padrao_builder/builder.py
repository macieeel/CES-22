from abc import ABC, abstractmethod

from products import Bolo


class AbstractBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_tipo_bolo(self, tipo):
        pass

    @abstractmethod
    def set_estilo_bolo(self, estilo):
        pass


class BoloBuilder(AbstractBuilder):
    def __init__(self):
        self.bolo = Bolo()

    def reset(self):
        self.bolo = Bolo()

    def set_tipo_bolo(self, tipo):
        self.bolo.set_tipo(tipo)

    def set_estilo_bolo(self, estilo):
        self.bolo.set_estilo(estilo)

    def get_resultado(self):
        return self.bolo

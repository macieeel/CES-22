from abc import ABC


class MotorAbstrato(ABC):
    def __init__(self):
        pass


class MotorEletrico(MotorAbstrato):
    def __init__(self):
        super().__init__()
        print("Motor Elétrico")


class MotorCombustao(MotorAbstrato):
    def __init__(self):
        super().__init__()
        print("Motor Combustão")


class MotorHibrido(MotorAbstrato):
    def __init__(self):
        super().__init__()
        print("Motor Híbrido")

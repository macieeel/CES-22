from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, price, mileage):
        self.brand = brand
        self.price = price
        self.mileage = mileage

    def set_price(self, price):
        self.price = price

    @abstractmethod
    # método que todas as classes terão que implementar
    def get_price(self):
        pass


class Moto(Vehicle):
    def get_price(self):
        print('Essa moto custa R$ {:.2f} reais'.format(*self.price))


class Car(Vehicle):
    def __init__(self, brand, price, mileage, sale=False):
        super().__init__(brand, price, mileage)
        self.sale = sale

    # metodo de instancia, tem acesso a propria instacia da classe
    def get_price(self):
        if self.sale:
            print('Esse carro custa R$ {:.2f} reais'.format(
                (1-self.sale)*self.price))
        else:
            print(('Esse carro custa R$ {:.2f} reais').format(*self.price))

    @classmethod
    # metodo de classe, nao tem acesso a instancia da classe, mas sim a propria classe
    def new_audi_on_sale(cls):
        return cls("Audi", 100000, 0, 0.1)

    @staticmethod
    # metodo estatico, nao tem nem acesso a instancia nem a classe
    def honk(sound):
        print(sound)


# metodos de classe e estaticos podem ser chamados diretamente da classe
audiTT = Car.new_audi_on_sale()
Car.honk("Bi bi")

# metodos de instancia precisam ter o objeto instanciado antes de serem chamados
audiTT.get_price()
audiTT.set_price(1000)
audiTT.get_price()

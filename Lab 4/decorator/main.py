# Template dado nos slides da aula


# Interface comum para objeto decorado e decoradores
class FoodComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


# Componente concreto, que receberá os decoradores
class Pizza(FoodComponent):
    cost = 0.0


# Superclasse dos decoradores
class Decorator(FoodComponent):
    def __init__(self, foodComponent):
        self.component = foodComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + FoodComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + " " + FoodComponent.getDescription(self)


# Decoradores concretos, bordas e sabores
class BordaRecheada(Decorator):
    cost = 0.25

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class BordaComum(Decorator):
    cost = 0.00

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class BordaEspecial(Decorator):
    cost = 0.50

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class Milho(Decorator):
    cost = 0.50

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class Marguerita(Decorator):
    cost = 0.75

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class QuatroQueijos(Decorator):
    cost = 1.00

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


class Vegetariana(Decorator):
    cost = 1.00

    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)


# Exemplos de Uso
milho_com_borda_recheada = Milho(BordaRecheada(Pizza()))
marguerita_com_borda_comum = Marguerita(BordaComum(Pizza()))
vegetariana_com_borda_recheada = Vegetariana(BordaRecheada(Pizza()))
vegetariana_com_borda_especial = Vegetariana(BordaEspecial(Pizza()))
quatro_queijos_com_borda_comum = QuatroQueijos(BordaComum(Pizza()))

print("\nExemplo Utilização Decorators\n")
print(milho_com_borda_recheada.getDescription() + ": $" +
      str(milho_com_borda_recheada.getTotalCost()))
print(marguerita_com_borda_comum.getDescription() + ": $" +
      str(marguerita_com_borda_comum.getTotalCost()))
print(vegetariana_com_borda_recheada.getDescription() + ": $" +
      str(vegetariana_com_borda_recheada.getTotalCost()))
print(vegetariana_com_borda_especial.getDescription() + ": $" +
      str(vegetariana_com_borda_especial.getTotalCost()))
print(quatro_queijos_com_borda_comum.getDescription() + ": $" +
      str(quatro_queijos_com_borda_comum.getTotalCost()))

print("\n")

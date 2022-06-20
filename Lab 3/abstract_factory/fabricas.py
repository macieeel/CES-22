from abc import ABC, abstractmethod

from produtos.concretos import BoloCenouraAniversario, BoloCenouraCasamento, BoloCenouraFesta, BoloChocolateAniversario, BoloChocolateCasamento, BoloChocolateFesta, BoloMandiocaAniversario, BoloMandiocaCasamento, BoloMandiocaFesta


class FabricaAbstrata(ABC):
    @abstractmethod
    def createBoloChocolate(self):
        pass

    @abstractmethod
    def createBoloMandioca(self):
        pass

    @abstractmethod
    def createBoloCenoura(self):
        pass


class FabricaBoloAniversario(FabricaAbstrata):
    def createBoloChocolate(self):
        super().createBoloChocolate()
        BoloChocolateAniversario()

    def createBoloMandioca(self):
        super().createBoloMandioca()
        BoloMandiocaAniversario()

    def createBoloCenoura(self):
        super().createBoloCenoura()
        BoloCenouraAniversario()


class FabricaBoloCasamento(FabricaAbstrata):
    def createBoloChocolate(self):
        super().createBoloChocolate()
        BoloChocolateCasamento()

    def createBoloMandioca(self):
        super().createBoloMandioca()
        BoloMandiocaCasamento()

    def createBoloCenoura(self):
        super().createBoloCenoura()
        BoloCenouraCasamento()


class FabricaBoloFesta(FabricaAbstrata):
    def createBoloChocolate(self):
        super().createBoloChocolate()
        BoloChocolateFesta()

    def createBoloMandioca(self):
        super().createBoloMandioca()
        BoloMandiocaFesta()

    def createBoloCenoura(self):
        super().createBoloCenoura()
        BoloCenouraFesta()

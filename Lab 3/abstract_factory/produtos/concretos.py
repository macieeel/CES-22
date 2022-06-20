from produtos.abstratos import BoloCenoura, BoloChocolate, BoloMandioca


class BoloChocolateAniversario(BoloChocolate):
    def __init__(self):
        super().__init__()
        print("Feliz Aniversário")


class BoloMandiocaAniversario(BoloMandioca):
    def __init__(self):
        super().__init__()
        print("Feliz Aniversário")


class BoloCenouraAniversario(BoloCenoura):
    def __init__(self):
        super().__init__()
        print("Feliz Aniversário")


class BoloChocolateCasamento(BoloChocolate):
    def __init__(self):
        super().__init__()
        print("Parabéns pelo Casamento")


class BoloMandiocaCasamento(BoloMandioca):
    def __init__(self):
        super().__init__()
        print("Parabéns pelo Casamento")


class BoloCenouraCasamento(BoloCenoura):
    def __init__(self):
        super().__init__()
        print("Parabéns pelo Casamento")


class BoloChocolateFesta(BoloChocolate):
    def __init__(self):
        super().__init__()
        print("Boa Festa")


class BoloMandiocaFesta(BoloMandioca):
    def __init__(self):
        super().__init__()
        print("Boa Festa")


class BoloCenouraFesta(BoloCenoura):
    def __init__(self):
        super().__init__()
        print("Boa Festa")

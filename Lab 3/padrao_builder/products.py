class Bolo:
    def __init__(self):
        self.tipo = None
        self.estilo = None

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_estilo(self, estilo):
        self.estilo = estilo

    def print(self):

        print("\nBolo de " + self.tipo)

        if self.estilo == "aniversario":
            print("Feliz Aniversário")

        if self.estilo == "casamento":
            print("Parabéns pelo Casamento")

        if self.estilo == "festa":
            print("Boa Festa")

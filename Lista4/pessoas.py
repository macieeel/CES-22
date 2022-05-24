class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Autor(Pessoa):
    def __init__(self, nome, email, titulos):
        super().__init__(nome, email)
        self.titulos = titulos


class Cliente(Pessoa):
    def __init__(self, nome, email, compras):
        super().__init__(nome, email)
        self.compras = compras

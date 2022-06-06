from abc import ABC, abstractmethod


class Produto:
    def __init__(self, preco_venda, preco_compra):
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra


class Imposto(ABC):
    @abstractmethod
    def get_imposto(self):
        pass


class Imposto1(Imposto):
    def __init__(self, genero, preco_venda, preco_compra):
        self.genero = genero
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra

    def get_imposto(self):
        print(50)


class Imposto2(Imposto):
    def __init__(self, genero='', preco_venda=0, preco_compra=0):
        self.genero = genero
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra

    def get_imposto(self):
        print(100)


class Livro(Produto):
    def __init__(self, titulo, autor, genero='', editora='', preco_venda=0, preco_compra=0, imposto=Imposto1):
        super().__init__(preco_venda, preco_compra)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editora = editora
        self.imposto = imposto(genero, preco_compra, preco_compra)

    def get_imposto(self):
        return self.imposto.get_imposto()

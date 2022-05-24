class Produto:
    def __init__(self, preco_venda, preco_compra):
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra


class Livro(Produto):
    def __init__(self, titulo, autor, genero='', editora='', preco_venda=0, preco_compra=0):
        super().__init__(preco_venda, preco_compra)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editora = editora
        self.imposto = Imposto(genero, preco_venda, preco_compra)

    def get_imposto(self):
        return self.imposto.get_imposto()


class Imposto:
    def __init__(self, genero, preco_venda, preco_compra):
        self.genero = genero
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra

    def get_imposto(self):
        pass

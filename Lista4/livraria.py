from abc import ABC, abstractmethod


class Livraria_Setor(ABC):
    def __init__(self, elemento):
        self.elemento = elemento

    @abstractmethod
    def inserir(self, elemento):
        pass

    @abstractmethod
    def remover(self, elemento):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def alterar(self, elemento, novo_elemento):
        pass


class Livraria_Setor_Clientes(Livraria_Setor):
    def __init__(self, clientes):
        self.clientes = clientes

    def inserir(self, cliente):
        self.clientes.append(cliente)

    def remover(self, cliente):
        self.clientes.remove(cliente)

    def listar(self):
        print("Clientes")
        for cliente in self.clientes:
            print(cliente.nome)
        print('\n')

    def alterar(self, cliente, cliente_alterado):
        index = self.clientes.index(cliente)
        self.clientes[index] = cliente_alterado


class Livraria_Setor_Livros(Livraria_Setor):
    def __init__(self, livros):
        self.livros = livros

    def inserir(self, livro):
        self.livros.append(livro)
        livro.autor.titulos.append(livro)

    def remover(self, livro):
        self.livros.remove(livro)

    def listar(self):
        print("Livros")
        for livro in self.livros:
            print(livro.titulo)
        print('\n')

    def alterar(self, livro, livro_alterado):
        index = self.livros.index(livro)
        self.livros[index] = livro_alterado

    def consultar_livros(self, autor):
        print(f"Livros de {autor.nome}:")
        for livro in self.livros:
            if livro.autor == autor:
                print(livro.titulo)
        print("\n")


class Livraria_Setor_Compras(Livraria_Setor):
    def __init__(self, compras, livros):
        self.compras = compras
        self.livros = livros

    def inserir(self, compra):
        for produto in compra.produtos_adquiridos:
            if not (produto[0] in self.livros):
                print("Produto(s) não disponível(is)\n")
                return
        self.compras.append(compra)
        compra.cliente.compras.append(compra)

    def remover(self, compra):
        self.compras.remove(compra)

    def listar(self):
        for compra in self.compras:
            compra.gerar_lista()

    def alterar(self, compra, compra_alterado):
        for produto in compra_alterado.produtos_adquiridos:
            if not (produto[0] in self.livros):
                print("Produto(s) não disponível(is)\n")
                return
        index = self.compras.index(compra)
        self.compras[index] = compra_alterado


class Livraria:
    def __init__(self, livros=[], clientes=[], compras=[]):
        self.setor_livros = Livraria_Setor_Livros(livros)
        self.setor_clientes = Livraria_Setor_Clientes(clientes)
        self.setor_compras = Livraria_Setor_Compras(compras, livros)

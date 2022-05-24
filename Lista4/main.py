
from livraria import Livraria
from produtos import Livro
from pessoas import Cliente, Autor
from compra import Compra


if __name__ == '__main__':
    Cultura = Livraria()

    Victor = Cliente("Victor", "v@gmail.com", [])
    Mauro = Cliente("Mauro", "m@gmail.com", [])
    Rafael = Cliente("Rafael", "r@gmail.com", [])

    George = Autor("George R R Martin", "georginho@gmail.com", [])
    JKRowling = Autor("J. K. Rowling", "jk@gmail.com", [])
    Tolkien = Autor("JRR Tolkien", "tolkinho@gmail.com", [])

    Livro1 = Livro("Winds of Winter", George, '', '', 50, 0)
    Livro2 = Livro("Clash of Kings", George, '', '', 50, 0)
    Livro3 = Livro("Harry Potter e a Pedra Filosofal",
                   JKRowling, '', '', 20, 0)
    Livro4 = Livro("Silmarillion", Tolkien, '', '', 79.9, 0)
    Livro5 = Livro("O Hobbit", Tolkien, '', '', 45.5, 0)

    # clientes
    Cultura.setor_clientes.inserir(Victor)
    Cultura.setor_clientes.inserir(Mauro)
    Cultura.setor_clientes.listar()

    Cultura.setor_clientes.alterar(Mauro, Rafael)
    Cultura.setor_clientes.listar()

    # livros
    Cultura.setor_livros.inserir(Livro1)
    Cultura.setor_livros.inserir(Livro2)
    Cultura.setor_livros.inserir(Livro3)
    Cultura.setor_livros.inserir(Livro4)
    Cultura.setor_livros.consultar_livros(George)
    Cultura.setor_livros.consultar_livros(JKRowling)
    Cultura.setor_livros.consultar_livros(Tolkien)
    Cultura.setor_livros.alterar(Livro4, Livro5)
    Cultura.setor_livros.consultar_livros(Tolkien)
    Cultura.setor_livros.listar()

    # compras
    Compra1 = Compra(Victor, [(Livro1, 2), (Livro2, 3)])
    Compra2 = Compra(Rafael, [(Livro3, 1)])
    Compra3 = Compra(Rafael, [(Livro5, 2)])
    Compra4 = Compra(Rafael, [(Livro4, 2)])
    Cultura.setor_compras.inserir(Compra1)
    Cultura.setor_compras.inserir(Compra2)
    Cultura.setor_compras.inserir(Compra3)
    Cultura.setor_compras.inserir(Compra4)
    Cultura.setor_compras.listar()

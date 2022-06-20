import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class Compra:
    def __init__(self, cliente, produtos_adquiridos):
        self.cliente = cliente
        self.produtos_adquiridos = produtos_adquiridos
        self.preco = 0

    def gerar_lista(self):
        print("Produto(s):")
        for produto in self.produtos_adquiridos:
            self.preco += produto[0].preco_venda * produto[1]
            print(
                f"  {produto[0].titulo}: {locale.currency(produto[0].preco_venda)} x{produto[1]}")
        print(f"Total: {locale.currency(self.preco)}\n")

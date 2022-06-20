from fabricas import FabricaAbstrata, FabricaBoloAniversario, FabricaBoloCasamento, FabricaBoloFesta


class Cliente:
    def __init__(self, fabrica: FabricaAbstrata):
        self.fabrica = fabrica()


print("\nAbstract Factory")
while(True):
    print("\n\nEscolha seu bolo:")
    print("Tipos: 1 - Chocolate, 2 - Mandioca, 3 - Cenoura")
    print("Estilos: 1 - Aniversário, 2 - Casamento, 3 - Festa\n")

    type = int(input("Digite o tipo que você quer: "))
    style = int(input("Digite o estilo que você quer: "))

    if type == 1:
        if style == 1:
            cliente = Cliente(FabricaBoloAniversario)
            cliente.fabrica.createBoloChocolate()
        elif style == 2:
            cliente = Cliente(FabricaBoloCasamento)
            cliente.fabrica.createBoloChocolate()
        elif style == 3:
            cliente = Cliente(FabricaBoloFesta)
            cliente.fabrica.createBoloChocolate()
        else:
            print("Inválido")
    elif type == 2:
        if style == 1:
            cliente = Cliente(FabricaBoloAniversario)
            cliente.fabrica.createBoloMandioca()
        elif style == 2:
            cliente = Cliente(FabricaBoloCasamento)
            cliente.fabrica.createBoloMandioca()
        elif style == 3:
            cliente = Cliente(FabricaBoloFesta)
            cliente.fabrica.createBoloMandioca()
        else:
            print("Inválido")
    elif type == 3:
        if style == 1:
            cliente = Cliente(FabricaBoloAniversario)
            cliente.fabrica.createBoloCenoura()
        elif style == 2:
            cliente = Cliente(FabricaBoloCasamento)
            cliente.fabrica.createBoloCenoura()
        elif style == 3:
            cliente = Cliente(FabricaBoloFesta)
            cliente.fabrica.createBoloCenoura()
        else:
            print("Inválido")
    else:
        print("Inválido")

    input("\nPrecione ENTER para escolher outro bolo...")

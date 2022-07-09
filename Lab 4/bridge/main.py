from fabrica import FabricaAbstrata, FabricaCaminhao, FabricaCarro, FabricaMoto


class Cliente:
    def __init__(self, fabrica: FabricaAbstrata):
        self.fabrica = fabrica()


print("\nVeículos - BRIDGE")
while(True):
    print("\n\nEscolha seu veículo:")
    print("Tipos: 1 - Carro, 2 - Caminhão, 3 - Moto")
    print("Motores: 1 - Combustão, 2 - Elétrico, 3 - Híbrido\n")

    type = int(input("Digite o tipo que você quer: "))
    engine = int(input("Digite o motor que você quer: "))

    if type == 1:
        if engine == 1:
            cliente = Cliente(FabricaCarro)
            cliente.fabrica.motorCombustao()
        elif engine == 2:
            cliente = Cliente(FabricaCarro)
            cliente.fabrica.motorEletrico()
        elif engine == 3:
            cliente = Cliente(FabricaCarro)
            cliente.fabrica.motorHibrido()
        else:
            print("Inválido")
    elif type == 2:
        if engine == 1:
            cliente = Cliente(FabricaCaminhao)
            cliente.fabrica.motorCombustao()
        elif engine == 2:
            cliente = Cliente(FabricaCaminhao)
            cliente.fabrica.motorEletrico()
        elif engine == 3:
            cliente = Cliente(FabricaCaminhao)
            cliente.fabrica.motorHibrido()
        else:
            print("Inválido")
    elif type == 3:
        if engine == 1:
            cliente = Cliente(FabricaMoto)
            cliente.fabrica.motorCombustao()
        elif engine == 2:
            cliente = Cliente(FabricaMoto)
            cliente.fabrica.motorEletrico()
        elif engine == 3:
            cliente = Cliente(FabricaMoto)
            cliente.fabrica.motorHibrido()
        else:
            print("Inválido")
    else:
        print("Inválido")

    input("Precione ENTER para escolher outro veiculo...")

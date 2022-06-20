
from director import Director
from builder import BoloBuilder

director = Director()
builder = BoloBuilder()
director.set_builder(builder)

print("\nPadrão Builder")
while(True):
    print("\n\nEscolha seu bolo:")
    print("Tipos: 1 - Chocolate, 2 - Mandioca, 3 - Cenoura")
    print("Estilos: 1 - Aniversário, 2 - Casamento, 3 - Festa\n")

    type = int(input("Digite o tipo que você quer: "))
    style = int(input("Digite o estilo que você quer: "))

    if type == 1:
        if style == 1:
            director.make_bolo_chocolate_aniversario()
            builder.get_resultado().print()
        elif style == 2:
            director.make_bolo_chocolate_casamento()
            builder.get_resultado().print()
        elif style == 3:
            director.make_bolo_chocolate_festa()
            builder.get_resultado().print()
        else:
            print("Inválido")
    elif type == 2:
        if style == 1:
            director.make_bolo_mandioca_aniversario()
            builder.get_resultado().print()
        elif style == 2:
            director.make_bolo_mandioca_casamento()
            builder.get_resultado().print()
        elif style == 3:
            director.make_bolo_mandioca_festa()
            builder.get_resultado().print()
        else:
            print("Inválido")
    elif type == 3:
        if style == 1:
            director.make_bolo_cenoura_aniversario()
            builder.get_resultado().print()
        elif style == 2:
            director.make_bolo_cenoura_casamento()
            builder.get_resultado().print()
        elif style == 3:
            director.make_bolo_cenoura_festa()
            builder.get_resultado().print()
        else:
            print("Inválido")
    else:
        print("Inválido")

    input("\nPrecione ENTER para escolher outro bolo...")
    builder.reset()

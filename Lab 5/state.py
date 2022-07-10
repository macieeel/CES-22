from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


class Document:
    def render(self):
        self.state.render()

    def publish(self):
        self.state.publish()

    def changeState(self, state: State):
        self.state = state


class Draft (State):
    def __init__(self, document: Document):
        super().__init__()
        self.document = document

    def render(self):
        super().render()
        global isAdmin
        if isAdmin == True:
            print("O documento foi renderizado")
        else:
            print("ERRO - Apenas disponível para administrador")

    def publish(self):
        super().publish()
        global isAdmin
        if isAdmin == True:
            self.document.changeState(Published(document))
            print("Documento Publicado")
        else:
            self.document.changeState(Moderation(document))
            print("Documento esperando aprovação")


class Moderation (State):
    def __init__(self, document: Document):
        super().__init__()
        self.document = document

    def render(self):
        super().render()
        global isAdmin
        if isAdmin == True:
            print("O documento foi renderizado")
        else:
            print("ERRO - Apenas disponível para administrador")

    def publish(self):
        super().publish()
        global isAdmin
        if isAdmin == True:
            validar = input("Deseja aprovar o documento? S/N ")
            if validar == "S":
                self.document.changeState(Published(document))
                print("Documento Publicado")
            elif validar == "N":
                self.document.changeState(Draft(document))
                print("Documento Reprovado")
            else:
                print("ERRO - Entrada inválida")

        else:
            print("Aguardando aprovação")


class Published (State):
    def __init__(self, document: Document):
        super().__init__()
        self.document = document
        self.description = "Publicado"

    def render(self):
        super().render()
        global isAdmin
        if isAdmin == True:
            print("Documento renderizado")
        else:
            print("ERRO - Apenas disponível para administrador")

    def publish(self):
        super().publish()
        global ans
        if time > 3:    # tempo de expiração
            print("Tempo de expiração alcançado. Documento em Rascunho")
            self.document.changeState(Draft(document))
        else:
            print("Documento já publicado\n")


document = Document()
document.changeState(Draft(document))


isAdmin = False
time = 0


while(True):
    user = input("\nÉ Administrador? S/N ")
    if user == "S":
        isAdmin = True
    elif user == "N":
        isAdmin = False
    else:
        print("Entrada inválida")

    print("\nSelecione uma operação:")
    option = input("Exibir documento - 1, Publicar Documento - 2: ")
    if option == "1":
        document.render()
    elif option == "2":
        document.publish()
    else:
        print("Entrada inválida")
    time += 1

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

# variaveis globais
extrato = ""
saldo = 0
historico_aux = ""


class Receiver:
    def __init__(self):
        pass

    def adicionar_ao_historico(self, texto):
        # função que adiciona operação ao histórico
        global historico_aux
        historico_aux = texto + "\n"
        historico.insert('1.0', historico_aux)

    def aumentar_saldo(self, valor, texto):
        # função que aumenta saldo e adiciona o valor ao histórico e ao extrato
        global historico_aux
        global saldo
        global extrato
        saldo = saldo + int(valor)
        historico_aux = texto + " R$ " + valor + ",00\n"
        historico.insert('1.0', historico_aux)
        extrato = extrato + historico_aux

    def diminuir_saldo(self, valor, pessoa, texto):
        # função que diminui saldo e adiciona o valor e a pessoa ao histórico e ao extrato
        global historico_aux
        global saldo
        global extrato
        saldo = saldo - int(valor)
        historico_aux = texto + "para " + pessoa + " de R$ " + valor + ",00\n"
        historico.insert('1.0', historico_aux)
        extrato = extrato + historico_aux

    def gerar_saldo(self):
        # função que que gera nova janela de saldo
        global saldo
        tela_saldo = Tk()
        tela_saldo.title("Saldo")
        tela_saldo.geometry("300x100")
        label_saldo = Label(
            tela_saldo, text="Seu saldo é de: R$ " + str(saldo) + ",00", font=(10))
        label_saldo.place(x=25, y=25)

    def gerar_extrato(self):
        # função que que gera nova janela de extrato
        global extrato
        global saldo
        tela_extrato = Tk()
        tela_extrato.title("Extrato")
        tela_extrato.geometry("450x400")
        extrato_text = Text(tela_extrato)
        extrato_text.place(x=25, y=75, width=400, height=300)
        label_extrato = Label(
            tela_extrato, text="Segue seu extrato:", font=(10))
        label_extrato.place(x=25, y=25)
        extrato_text.insert('1.0', extrato + '\n\nSaldo Final: ' + str(saldo))


receiver = Receiver()


class Command(ABC):
    # classe abstratas para as operações
    @abstractmethod
    def execute(self):
        pass


class VerficarSaldo(Command):
    def __init__(self, texto):
        super().__init__()
        self.receiver = receiver
        self.texto = texto

    def execute(self):
        super().execute()
        receiver.gerar_saldo()
        receiver.adicionar_ao_historico(self.texto)


class VerficarExtrato(Command):
    def __init__(self, texto):
        super().__init__()
        self.receiver = receiver
        self.texto = texto

    def execute(self):
        super().execute()
        receiver.gerar_extrato()
        receiver.adicionar_ao_historico(self.texto)


class Tranferencia(Command):
    def __init__(self, texto):
        super().__init__()
        self.receiver = receiver
        self.texto = texto

    def execute(self):
        super().execute()
        self.valor = valor_transferencia.get()
        self.pessoa = pessoa_transferencia.get()
        receiver.diminuir_saldo(self.valor, self.pessoa, self.texto)


class Depositar(Command):
    def __init__(self, texto):
        super().__init__()
        self.receiver = receiver
        self.texto = texto

    def execute(self):
        super().execute()
        self.valor = valor_deposito.get()
        receiver.aumentar_saldo(self.valor, self.texto)


# Definições da tela
tela = Tk()
tela.title("Banco - Victor Maciel")
tela.geometry("650x400")

valor_transferencia = Entry()
pessoa_transferencia = Entry()
valor_deposito = Entry()
pessoa_transferencia = Entry()
valor_transferencia.insert(END, "Insira um valor")
pessoa_transferencia.insert(END, "Insira uma pessoa")
valor_deposito.insert(END, "Insira um valor")
historico_nome = Label(tela, text="Histórico")
historico = Text()
label = Label(
    tela, text="Selecione uma das operações abaixo", font=(10))


# Definições dos botões, que funcionam como invokers
buttton_saldo = Button(tela, text="Verificar Saldo",
                       command=VerficarSaldo("Checagem de Saldo").execute)
button_extrato = Button(tela, text="Verificar Extrato",
                        command=VerficarExtrato("Checagem de Extrato").execute)
button_transferencia = Button(tela, text="Transferir",
                              command=Tranferencia("Transfência: ").execute)
button_depositar = Button(tela, text="Depósitar",
                          command=Depositar("Depósito:").execute)


# posicionamento dos items
label.place(x=25, y=25)

historico_nome.place(x=225, y=75)
historico.place(x=225, y=100, width=400, height=275)
valor_transferencia.place(x=550, y=215)
pessoa_transferencia.place(x=550, y=190)


buttton_saldo.place(x=25, y=75)
button_extrato.place(x=25, y=125)

button_transferencia.place(x=25, y=175)
valor_transferencia.place(x=25, y=240)
pessoa_transferencia.place(x=25, y=215)

button_depositar.place(x=25, y=290)
valor_deposito.place(x=25, y=330)

# loop
tela.mainloop()

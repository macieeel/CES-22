from builder import AbstractBuilder


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    # casamento
    def make_bolo_chocolate_casamento(self):
        self.builder.set_tipo_bolo("Chocolate")
        self.builder.set_estilo_bolo("casamento")

    def make_bolo_mandioca_casamento(self):
        self.builder.set_tipo_bolo("Mandioca")
        self.builder.set_estilo_bolo("casamento")

    def make_bolo_cenoura_casamento(self):
        self.builder.set_tipo_bolo("cenoura")
        self.builder.set_estilo_bolo("casamento")

    # aniversario
    def make_bolo_chocolate_aniversario(self):
        self.builder.set_tipo_bolo("Chocolate")
        self.builder.set_estilo_bolo("aniversario")

    def make_bolo_mandioca_aniversario(self):
        self.builder.set_tipo_bolo("Mandioca")
        self.builder.set_estilo_bolo("aniversario")

    def make_bolo_cenoura_aniversario(self):
        self.builder.set_tipo_bolo("Cenoura")
        self.builder.set_estilo_bolo("aniversario")

    # festa
    def make_bolo_chocolate_festa(self):
        self.builder.set_tipo_bolo("Chocolate")
        self.builder.set_estilo_bolo("festa")

    def make_bolo_mandioca_festa(self):
        self.builder.set_tipo_bolo("Mandioca")
        self.builder.set_estilo_bolo("festa")

    def make_bolo_cenoura_festa(self):
        self.builder.set_tipo_bolo("Cenoura")
        self.builder.set_estilo_bolo("festa")

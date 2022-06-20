class Carro():
    def mover(self):
        print('Andando...')


class Aviao():
    def mover(self):
        print('Voando...')


class CarroVoador(Aviao, Carro):
    def iniciar(self):
        super().mover()


carro = CarroVoador()
carro.mover()
# Voando...

''' Isso acontece pois como Aviao vem antes de Carro na definicao
    de CarroVoador, seu metodo mover() é o que tem a prioridade
'''

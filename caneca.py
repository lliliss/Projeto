from produto import *

class Caneca(Produto):
    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        self.capacidade = valores[3]
        if valores[4] == 0:
            self.gerar_numero_serie(3)
        else:
            global n_series
            n_series.append(valores[4])
            self.numero_serie = valores[4]
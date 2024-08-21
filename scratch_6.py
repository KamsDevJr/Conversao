class RelogiodeBolso:
    def __init__(self, cor, tamanho, tipo_ponteiro, referencia):
        self.cor = cor
        self.tamanho = tamanho
        self.tipo_ponteiro = tipo_ponteiro
        self.referencia = referencia


relogio_debolso = RelogiodeBolso("dourado", "2cm", "vintage", "distorcido")
print(relogio_debolso.referencia)

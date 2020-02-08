class Publicacio():
    def __init__(self, referencia, titol):
        self.referencia = referencia
        self.titol = titol

    def retornaReferencia(self):
        return self.referencia

    def retornaTitol(self):
        return self.titol

    def setReferencia(self, referencia):
        self.referencia = referencia

    def setTitol(self, titol):
        self.titol = titol

    def visualitza(self):
        print ("Numero de referencia: {}".format(self.retornaReferencia()))
        print ("Titol de la publicacio: {}".format(self.retornaTitol()))

    def __str__(self):
        return str(self.referencia)

    def __eq__(self, other):
        return self.referencia == other


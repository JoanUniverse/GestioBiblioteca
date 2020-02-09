from model.Obra import Obra


class Volum(Obra):
    def __init__(self, nro, autor, nrePags, referencia, titol):
        Obra.__init__(self, autor, nrePags, referencia, titol)
        self.nro = nro

    def retornaNro(self):
        return self.nro

    def setNro(self, nro):
        self.nro = nro

    def visualitza(self):
        super(Volum, self).visualitza()
        print "---------- Volum ----------"
        print "Numero del volum: {}".format(self.nro)

    def __str__(self):
        return "Numero de volum: {}".format(self.nro)

    def __eq__(self, other):
        return self.referencia == other
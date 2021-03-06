from model.Publicacio import Publicacio


class Revista(Publicacio):
    def __init__(self, any, nro, referencia, titol):
        Publicacio.__init__(self, referencia, titol)
        self.any = any
        self.nro = nro

    def retornaAny(self):
        return self.any

    def retornaNro(self):
        return  self.nro

    def setAny(self, any):
        self.any = any

    def setNro(self, nro):
        self.nro = nro

    def visualitza(self):
        super(Revista, self).visualitza()
        print "---------- Revista ----------"
        print ("Any de la revista: {}".format(self.retornaAny()))
        print ("Numero de revista: {}".format(self.retornaNro()))

    def __str__(self):
        return "Any: {}, Numero: {}".format(self.any, self.nro)

    def __eq__(self, other):
        return self.referencia == other
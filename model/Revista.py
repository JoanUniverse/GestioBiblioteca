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
        print ("Any de la revista: {}".format(self.retornaAny()))
        print ("Numero de revista: {}".format(self.retornaNro()))

    def __str__(self):
        return self.referencia

    def __eq__(self, other):
        return self.referencia == other

# r = Revista(2000, 11, 13, "Hola")
# r.visualitza()
from model.Publicacio import Publicacio


class Obra(Publicacio):
    def __init__(self, autor, nrePags, referencia, titol):
        Publicacio.__init__(self, referencia, titol)
        self.autor = autor
        self.nrePags = nrePags

    def retornaAutor(self):
        return self.autor

    def retornaNrePags(self):
        return self.nrePags

    def setAutor(self, autor):
        self.autor = autor

    def setNrePags(self, nrePags):
        self.nrePags = nrePags

    def visualitza(self):
        super(Obra, self).visualitza()
        print "---------- Obra ----------"
        print ("Nom de l'autor: {}".format(self.retornaAutor()))
        print ("Nombre de pagines de l'obra: {}".format(self.retornaNrePags()))

    def __str__(self):
        return "Autor: {}, Pagines: {}".format(self.autor, self.nrePags)

    def __eq__(self, other):
        return self.referencia == other
from model.Publicacio import Publicacio


class Biblioteca():
    publicacions = []

    def __init__(self, capacitat):
        self.capacitat = capacitat

    def coneixCapacitat(self):
        return self.capacitat

    def nombreElements(self):
        print "numero elements"

    def afegirPublicacio(self, referencia, titol):
        if len(self.publicacions) < self.capacitat:
            if self.comprovaRepetides(referencia):
                p = Publicacio(referencia, titol)
                self.publicacions.append(p)
                print "Publicacio afegida"
            else:
                print "La aquesta publicacio ja existeix"
        else:
            print "Capacitat maxima, no es pot afegir"

    def cercaPublicacio(self, referencia):
        for p in self.publicacions:
            if p.retornaReferencia() == referencia:
                print "Publicacio trobada"
                return p
        print "La publicacio amb aquesta referencia no existeix"
        return ""

    def mostraPublicacio(self, referencia):
        print self.cercaPublicacio(referencia)

    def comprovaRepetides(self, referencia):
        for p in self.publicacions:
            if p.retornaReferencia() == referencia:
                return False
        return True

b = Biblioteca(5)
b.afegirPublicacio(1, "Primera")
b.afegirPublicacio(2, "Segona")
b.afegirPublicacio(3, "Tercera")
b.afegirPublicacio(4, "Cuarta")
b.afegirPublicacio(5, "Quinta")
b.afegirPublicacio(6, "Sisena")
b.mostraPublicacio(5)




import sys #He importat sys per poder sortir de l'aplicacio

from model.Publicacio import Publicacio


class Biblioteca():
    publicacions = []

    def __init__(self, capacitat):
        self.capacitat = capacitat

    def coneixCapacitat(self):
        return self.capacitat

    def nombreElements(self):
        if len(self.publicacions) == 0:
            nombre = 0
        else:
            nombre = len(self.publicacions)
        print "Hi ha un total de {} publicacions!".format(nombre)

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
            if str(p.retornaReferencia()) == referencia:
                print "Publicacio trobada"
                return p
        print "La publicacio amb aquesta referencia no existeix"
        return ""

    def mostraPublicacio(self, referencia):
        print self.cercaPublicacio(referencia)

    def visualitzaBiblioteca(self):
        if len(self.publicacions) == 0:
            print "No hi ha cap publicacio a la biblioteca"
        for p in self.publicacions:
            p.visualitza()

    def comprovaRepetides(self, referencia):
        for p in self.publicacions:
            if p.retornaReferencia() == referencia:
                return False
        return True

#Cream la biblioteca que tendra una capacitat fixa
b = Biblioteca(5)
clear = "\n" * 100 #Fa bots de linea per "Borrar" el contingut de la consola anteriorment impres
#MENU
while(True):
    print "---------------------- MENU ----------------------"
    print "Que vols fer?"
    print "1. Veure capacitat de la biblioteca"
    print "2. Mostrar nombre d'elements que hi ha a la biblioteca"
    print "3. Afegir publicacio a la biblioteca"
    print "4. Mostrar publicacio"
    print "5. Visualitzar contingut de la biblioteca"
    print "6. Surt"
    opcio = str(raw_input())
    if opcio == "1":
        print "Capacitat de la biblioteca: " + str(b.coneixCapacitat())
        espera = raw_input() #Enter per continuar
    elif opcio == "2":
        b.nombreElements()
        espera = raw_input()
    elif opcio == "3":
        print clear
        print "Quina referencia te la publicacio?"
        referencia = input()
        print "Quin titol te la publicacio?"
        titol = str(raw_input())
        b.afegirPublicacio(referencia, titol)
        espera = raw_input()
    elif opcio == "4":
        cerca = raw_input("Quina publicacio vols veure?")
        b.mostraPublicacio(cerca)
        espera = raw_input()
    elif opcio == "5":
        print clear
        b.visualitzaBiblioteca()
        espera = raw_input()
    elif opcio == "6":
        print "Adeu"
        sys.exit(0)
    else: 
        print "Opcio desconeguda, torna a insertar la opcio"
        espera = raw_input()
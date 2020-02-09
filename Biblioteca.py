import sys #He importat sys per poder sortir de l'aplicacio

from model.Publicacio import Publicacio
from model.Obra import Obra
from model.Revista import Revista
from model.Volum import Volum


class Biblioteca():
    publicacions = []

    def __init__(self, capacitat):
        self.capacitat = capacitat

    def coneixCapacitat(self):
        return self.capacitat

    #Aquest metode mira el numero de publicacions que hi ha a la bibioteca
    #Si la len() de la list es 0, ens diu que hi ha 0 publicacion (Control d'errades)
    #Sino, ens diu el nombre de publicacions que hi ha
    def nombreElements(self):
        if len(self.publicacions) == 0:
            nombre = 0
        else:
            nombre = len(self.publicacions)
        print "Hi ha un total de {} publicacions!".format(nombre)

    #Si la len() de la list es menos que la capacitat de la biblioteca, vol dir que podem afegir una publicacio
    #Tambe li passam la referencia al metode comprovaRepetides() per mirar si ja existeix
    #Si ha passat els dos ifs, insereix la publicacio (.append())
    def afegirPublicacio(self, p):
        if len(self.publicacions) < self.capacitat:
            if self.comprovaRepetides(p.retornaReferencia()):
                self.publicacions.append(p)
                print "Publicacio afegida"
            else:
                print "La aquesta publicacio ja existeix"
        else:
            print "Capacitat maxima, no es pot afegir"

    #Recorr totes les publicacions creades i cerca la que coincideix amb la referencia passada
    #per parametre
    def cercaPublicacio(self, referencia):
        for p in self.publicacions:
            if str(p.retornaReferencia()) == referencia:
                print "Publicacio trobada"
                return p
        print "La publicacio amb aquesta referencia no existeix"
        return ""

    #Mostra la publicacio que ha trobat al metode cercaPublicacio()
    def mostraPublicacio(self, referencia):
        print self.cercaPublicacio(referencia)

    #Si no hi ha cap publicacio fa un print, en canvi si n'hi ha
    #mostra el metode visualitza de cada publicacio
    def visualitzaBiblioteca(self):
        if len(self.publicacions) == 0:
            print "No hi ha cap publicacio a la biblioteca"
        for p in self.publicacions:
            p.visualitza()
            print "\n"

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
    print "Tria la operacio que vols realitzar:"
    print "1. Veure capacitat de la biblioteca"
    print "2. Mostrar nombre d'elements que hi ha a la biblioteca"
    print "3. Afegir publicacio a la biblioteca"
    print "4. Mostrar publicacio"
    print "5. Visualitzar contingut de la biblioteca"
    print "6. Surt"
    #Depenent de l'opcio que s'introdueixi entrara a un if o l'altre, si no n'entra a cap i arriba a
    #l'else, ens diu que has introduit una opcio que no es correcte
    opcio = str(raw_input())
    if opcio == "1":
        print "Capacitat de la biblioteca: " + str(b.coneixCapacitat())
        espera = raw_input() #Enter per continuar
    elif opcio == "2":
        b.nombreElements()
        espera = raw_input()
    elif opcio == "3":
        print clear
        #Quan afegeixes una publicacio, he considerat que cada vegada que introdueixis una obra o una
        #revista ja crees una publicacio instantaneament, per tant simplement don dues opcions, obra, revista o volum
        print "Que vols afegir, una obra, una revista o un volum? \n" \
              "1. Obra \n" \
              "2. Revista \n" \
              "3. Volum"
        tria = str(raw_input())
        #Si tries la primera opcio crees una obra i l'afegeixes a la llista
        if tria == "1":
            print "Quina referencia te la publicacio?"
            referencia = input()
            print "Quin titol te la publicacio?"
            titol = str(raw_input())
            print "Quin autor te l'obra?"
            autor = str(raw_input())
            print "Quantes pagines te?"
            pagines = str(raw_input())
            o = Obra(autor, pagines, referencia, titol)
            b.afegirPublicacio(o)
            espera = raw_input()
        # Si tries la segona opcio crees una revista i l'afegeixes a la llista
        elif tria == "2":
            print "Quina referencia te la publicacio?"
            referencia = input()
            print "Quin titol te la publicacio?"
            titol = str(raw_input())
            print "De quin any es la revista?"
            any = str(raw_input())
            print "Numero de revista?"
            nro = str(raw_input())
            r = Revista(any, nro, referencia, titol)
            b.afegirPublicacio(r)
            espera = raw_input()
        # Si tries la tercera opcio crees un volum i l'afegeixes a la llista
        elif tria == "3":
            print "Quina referencia te la publicacio?"
            referencia = input()
            print "Quin titol te la publicacio?"
            titol = str(raw_input())
            print "Quin autor te l'obra?"
            autor = str(raw_input())
            print "Quantes pagines te?"
            pagines = str(raw_input())
            print "Quin es el numero del volum?"
            nrov = str(raw_input())
            v = Volum(nrov, autor, pagines, referencia, titol)
            b.afegirPublicacio(v)
            espera = raw_input()
        #Com en el menu principal, si la opcio que ha donat l'usuari no coincideix amb cap de l'if,
        #ens diu que no s'ha pogut reconeixer la opcio
        else:
            print "Opcio desconeguda, torna a insertar la opcio"
            espera = raw_input()
    #Et demana quina referencia vols cercar a la llista i la passa com a parametre al metode mostraPublicacio()
    elif opcio == "4":
        cerca = raw_input("Quina publicacio vols veure?")
        b.mostraPublicacio(cerca)
        espera = raw_input()
    elif opcio == "5":
        print clear
        b.visualitzaBiblioteca()
        espera = raw_input()
    #Aqui faig us de l'import de sys per poder sortir del programa (Va ser la opcio que vaig veure que podia fer)
    elif opcio == "6":
        print "Adeu"
        sys.exit(0)
    else:
        print "Opcio desconeguda, torna a insertar la opcio"
        espera = raw_input()
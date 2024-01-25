#Vytvořte třídu Slon. Slon má několik atributů: jméno, barvu, váhu a povolání.
# (Pokud je to moc těžké, stačí jen dva atributy místo čtyř)Slon umí dvě 
# činnosti: troubit a stříkat 

class Slon:
    def __init__(self, jmeno, barva, vaha, povolani):
        self.jmeno = jmeno
        self.barva = barva
        self.vaha = vaha
        self.povolani = povolani

    def trub(self):
        print("1 vlastnost:\t")
        print("TUUUUU TUuuu tuuuu ")
        
    
    def strikej(self):
        print("2 vlastnost:\t")

        if self.barva == "růžový":
            self.usmev()
        else:
            print("Stříkám proud vody")
        
    def usmev(self):
        print("HE HE HE HE ")

    def jit_spat(self):
        print("slon usnul")
# Vytvořte jednu instanci slona a uložte ho do proměnné.
# Nechte ho zatroubit a postříkat lidi.Vypište jeho jméno, pak ho přejmenujte a vypište nové jméno.

ferda = Slon("Ferda","modrý","200","hlídač")
print( "Řádek 17:\n vypsání 4 atributů\t" + ferda.jmeno + "," + ferda.barva + "," + ferda.vaha + "," + ferda.povolani)


ferda.trub() 
ferda.strikej()
 
# přejmenování
ferda.jmeno = "Chobůtek"
print(f"řádek:26 \n\t Už to není ferda, jmenuje se: {ferda.jmeno}")

# Vytvořte druhou a třetí instanci slona. Vypište povolání druhého slona, pak povolání změňte a znovu 
# ho vypište.

bobik = Slon("Bobík","růžový","váha:350kg","lenoch")
smolik = Slon("Smolík","zelený","váha:400kg","sportovec")

print(f"řádek 36:\n\t Povolání slona Bobíka:\n\t{bobik.povolani}")
bobik.povolani = "mazel"
print(f"řádek 36:\n\tBobík už  není lenoch, je to:\n\t{bobik.povolani}")

#BONUS pro pokročilé:Pokud je slon růžový, místo stříkání vody se bude jen usmívat.
# (růžoví sloni přeci nejsou tak škodolibí.)

# seznam slonů
sloni = [
    Slon("Ferda","modrý","200","hlídač"),
    Slon ("Bobík","růžový","váha:350kg","lenoch"),
    Slon ("Smolík","zelený","váha:400kg","sportovec"),
]

# cyklus pro každého slona
for slon in sloni:
    print(f"řádek 60:\n\t{slon.jmeno} , barva:{slon.barva}")
    slon.strikej()
    
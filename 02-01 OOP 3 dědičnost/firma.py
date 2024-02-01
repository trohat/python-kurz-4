
class Clovek:
    def __init__(self, jmeno, prijmeni):
        if jmeno == "xxx":
            raise ValueError("Zakázané jméno")
        if prijmeni == "yyy":
            raise ValueError("Zakázané příjmení")
        if jmeno == "Hynek":
            print("Vše nejlepší ke svátku")
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def jit_do_prace(self):
        print("Jdu do práce. Těším se. :)")

karel = Clovek("Karel", "Procházka")

class Zamestnanec(Clovek):
    def vyrabej_neco(self):
        print("Vyrobil jsem spoustu nových věcí.")

    def dojdi_si_pro_výplatu(self):
        print("Dostal jsem výplatu.")
        print("Jupííí, jsem bohatej!!")

michal = Zamestnanec("Michal", "Novák")

class Programator(Zamestnanec):
    def __init__(self, jmeno, prijmeni, programovaci_jazyk): # overriding - přepsat, nebo taky přebít, překrýt
        super().__init__(jmeno, prijmeni) # super znamená superclass, tedy jiný název pro rodičovskou třídu
        self.programovaci_jazyk = programovaci_jazyk

    def vyrabej_neco(self):
        print("Vyrobil jsem nový program.")

    def programuj(self):
        print(f"Naprogramoval jsem super aplikaci v jazyce {self.programovaci_jazyk}.")

    def ucit_se(self):
        print("Naučil jsem se nové triky a vylepšil jsem náš starý kód.")

filip = Programator("Filip", "Kučera", "Python")
hynek = Programator("Hynek", "Kučera", "Python")

print(hynek.jmeno, hynek.prijmeni)
filip.programuj()
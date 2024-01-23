class Slon:
    def __init__(self, jmeno, barva, vaha, povolani):
        self.jmeno = jmeno
        self.barva = barva
        self.vaha = vaha
        self.povolani = povolani

    def troubit(self):
        print("tůůůůů")

    def strikat_na_lidi(self):
        if self.barva == "růžový":
            print("ahoj, všechny vás zdravím s úsměvem :)")
        else:
            print("všichni kolem jste mokří")

    def jdi_do_cirkusu(self):
        print("Jdu do cirkusu.")
        print(self)
        print(f"Moje povolání je {self.povolani}.")
        self.troubit()
        self.strikat_na_lidi()
        self.troubit()
        print("Moc se mi tu líbilo.")

    def __str__(self):
        return f"Já jsem {self.barva} {self.jmeno}."

slon1 = Slon("Jumbo", "modrý", 50, "klaun")
slon2 = Slon("Dumbo", "šedivý", 60, "vozí lidi")
slon3 = Slon("Rafael", "bílý", 70, "kouká kolem sebe")
slon4 = Slon("Karel", "růžový", 40, "usmívat se")

slon4.troubit()


seznam_slonu = [slon1, slon2, slon3, slon4]

for slon in seznam_slonu:
    slon.jdi_do_cirkusu()
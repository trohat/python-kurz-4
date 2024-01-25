from auto import auto1, auto2, auto3

class Clovek():
    def __init__(self, jmeno, povolani, auto):
        self.jmeno = jmeno
        self.povolani = povolani
        self.auto = auto

    def ridit_svoje_auto(self):
        if self.auto == None:
            print("Není co řídit")
        else:
            self.auto.jet("jen tak", 2)

    def ridit_cizi_auto(self, cizi_auto):
        cizi_auto.jet("daleko", 20)

    def __str__(self):
        return f"Jsem {self.povolani} {self.jmeno}."

adam = Clovek("Adam", "učitel", auto1)
bedrich = Clovek("Bedřich", "instalatér", auto2)
kamil = Clovek("Kamil", "zedník", auto2)


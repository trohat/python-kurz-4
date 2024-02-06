from zvire import *

class Klec:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.seznam_zvirat = []

    def pridej_zvire(self, zvire):
        self.seznam_zvirat.append(zvire)

    def pridej_vice_zvirat_najednou(self, *args):
        for zvire in args:
            self.pridej_zvire(zvire)

    def __str__(self):
        retezec = f"Jsem klec jménem {self.jmeno} a jsou ve mě tato zvířata: "
        for zvire in self.seznam_zvirat:
            if isinstance(zvire, Opice):
                retezec += zvire.jmeno
            else:
                retezec += f"{zvire.barva[:-1]}ý {zvire.__class__.__name__.lower()}"
            retezec += ", "
        return retezec[:-2]
    
klec1 = Klec("Pavilon opic")

klec1.pridej_zvire(rozarka)
print(klec1)
klec1.pridej_vice_zvirat_najednou(agatka, filip)
print(klec1)

klec2 = Klec("Pavilon hadů")
klec2.pridej_vice_zvirat_najednou(zmije, anakonda, hroznys)
print(klec2)

klec3 = Klec("Pavilon slonů")
klec3.pridej_vice_zvirat_najednou(slon1, slon2, slon3)
print(klec3)
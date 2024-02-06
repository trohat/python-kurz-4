from klec import klec1, klec2, klec3

class Zoo:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.klece_v_zoo = []

    def pridej_klec(self, klec):
        self.klece_v_zoo.append(klec)

    def pridej_vice_kleci_najednou(self, *args):
        for klec in args:
            self.pridej_klec(klec)

    def vypis_podle_barvy(self, barva):
        print(f"Vypisuji zvířata s barvou", barva)
        for pavilon in self.klece_v_zoo:
            for zvire in pavilon.seznam_zvirat:
                if zvire.barva == barva:
                    print(zvire)

    def __str__(self):
        pocet_zvirat = 0
        for pavilon in self.klece_v_zoo:
            pocet_zvirat += len(pavilon.seznam_zvirat)
        retezec = f"Jsem {self.jmeno}, mám {len(self.klece_v_zoo)} pavilony a v nich {pocet_zvirat} zvířat."
        return retezec
        


zoo = Zoo("Zoo Praha")

zoo.pridej_vice_kleci_najednou(klec1, klec2, klec3)
print(zoo)

zoo.vypis_podle_barvy("rezavá")
zoo.vypis_podle_barvy("modrá")
zoo.vypis_podle_barvy("šedá")
zoo.vypis_podle_barvy("černá")
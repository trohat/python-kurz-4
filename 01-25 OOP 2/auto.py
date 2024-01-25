
class Auto:
    def __init__(self, znacka, barva, akt_benzin, max_benzin):
        """
        akt_benzin = kolik je teď benzínu v nádrži
        max_benzin = kolik může být maximálně benzinu v nádrži
        """
        self.znacka = znacka
        self.barva = barva
        self.akt_benzin = akt_benzin
        self.max_benzin = max_benzin

    def jet(self, cil_vyletu, spotreba):
        """
        cil_vyletu = kam pojedeme
        spotreba = kolik spotrebujeme na výletě benzínu
        """
        if (spotreba > self.akt_benzin):
            print("Nikam nejedeme.")
        else:
            print(f"Jedeme {cil_vyletu}.")
            self.akt_benzin = self.akt_benzin - spotreba

    def natankovat(self):
        """
        když tankujeme, vždy bereme plnou nádrž
        """
        self.akt_benzin = self.max_benzin

    def __str__(self):
        return f"Jsem {self.barva} {self.znacka} a v nádrži o velikosti {self.max_benzin} mám {self.akt_benzin} litrů."


auto1 = Auto("Škodovka", "modrá", 10, 60)
auto2 = Auto("Opel", "oranžový", 2, 70)
auto3 = Auto("Toyota RAV4", "červená", 79, 80)

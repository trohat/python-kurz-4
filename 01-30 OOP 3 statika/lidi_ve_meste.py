
class Clovek:
    def __init__(self, jmeno, prijmeni, vyska, vaha):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vyska = vyska
        self.vaha = vaha

    def __repr__(self):
        return f"{self.jmeno} {self.prijmeni}"  

    def __str__(self):
        return f"Já jsem {self.jmeno} {self.prijmeni} a vážím {self.vaha} kg."
    

class Mesto:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.seznam_obyvatel = []

    def pridej_cloveka(self, clovek):
        if isinstance(clovek, Clovek):
            self.seznam_obyvatel.append(clovek)
        else:
            print("Nelze přidat, není to člověk.")

    def pridej_lidi(self, *lidi): # většinou se píše jako *args
        for clovek in lidi:
            if isinstance(clovek, Clovek):
                self.seznam_obyvatel.append(clovek)
            else:
                print("Nelze přidat, není to člověk.")

    def __str__(self):
        popis_mesta = f"\nJá jsem město {self.jmeno}.\nA bydlí tu tihle lidé: "
        popis_mesta += str(self.seznam_obyvatel)
        # for clovek in self.seznam_obyvatel:
        #     popis_mesta += f"{clovek.jmeno} {clovek.prijmeni}, "
        # popis_mesta = popis_mesta[:-2] + "."
        return popis_mesta

adam = Clovek("Adam", "Růžička", 180, 70)
bedrich = Clovek("Bedřich", "Fiala", 190, 93)
katka = Clovek("Katka", "Pivoňková", 160, 52)

praha = Mesto("Praha")

praha.pridej_lidi(adam, bedrich, Clovek("Cyril", "Karafiát", 185, 52))

print("Tisknu lidi v Praze:")
for clovek in praha.seznam_obyvatel:
    print(clovek)

print(praha)
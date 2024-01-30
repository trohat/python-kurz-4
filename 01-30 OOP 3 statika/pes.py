# statika = něco patří ne instanci, ale celé třídě

class Pes:
    pocet_pejsku = 0
    seznam_psu = []

    def __init__(self, jmeno, rasa):
        self.jmeno = jmeno
        self.rasa = rasa
        # self.__class__.pocet_pejsku += 1
        Pes.pocet_pejsku += 1
        Pes.seznam_psu.append(self)

    def __str__(self):
        return f"Toto je {self.rasa} {self.jmeno}."
    
    def stekej(self):
        return f"{self.jmeno} dělá: Haf haf haf."
    
    @staticmethod
    def vypis_pocet_psu():
        print("Počet psů je ", end="")
        print(str(Pes.pocet_pejsku) + ".")

    @classmethod
    def vypis_pocet_psu_jinak(cls):
        print("Počet psů je ", end="♥♥💑♥")
        print(str(cls.pocet_pejsku) + ".")
    


pes1 = Pes("Alík", "vlčák")
pes2 = Pes("Rex", "bernardýn")
pes3 = Pes("Filip", "jezevčík")
pes4 = Pes("Filip", "jezevčík")

for i in range(100):
    pes4 = Pes("Filip", "jezevčík")

print(pes1.jmeno)

# print(Pes.pocet_pejsku)

Pes.vypis_pocet_psu_jinak()

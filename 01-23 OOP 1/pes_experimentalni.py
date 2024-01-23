# toto je soubor ve kterém jsme si jen hráli, neděste se toho :))))

class Pes:
    def __init__(self, jmeno, *args, **kwargs):
        self.jmeno = jmeno
        if len(args) == 2:
            self.rasa = args[0]
            self.vaha = args[1]

    def stekej(self):
        print("Haf haf haf, bojíte se mě?")

    def kousej(self):
        print("Ukousnul jsem ti kus nohavice.")

    def udelej_printy(self):
        print(self.jmeno)
        print(self.rasa)
        self.stekej()

    def __lt__(self, other):
        return self.vaha < other.vaha
    
    def __repr__(self):
        return f"{self.jmeno} {self.rasa} {self.vaha}"


alik1 = Pes("Alík", "vlčák", 20)    
alik2 = Pes("Rex", "bernardýn", 3)
alik3 = Pes("Filip", "jezevčík", 5)
alik4 = Pes("Jakub", "jfezevčík", 50)

psi = [alik1, alik2, alik3, alik4]
psi.sort()
print(psi)

def udelej_printy(pes):
    print(pes.jmeno)
    print(pes.rasa)
    pes.stekej()

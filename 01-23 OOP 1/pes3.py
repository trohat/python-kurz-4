# jdeme vytvořit třídu Pes, což je továrna (vzor) pro výrobu psů
# metoda __init__ je takzvaná dunder metoda, což je zkratka pro "double underscore"

class Pes:
    def __init__(self, jmeno, rasa):
        self.jmeno = jmeno
        self.rasa = rasa

    def stekej(self):
        print("Haf haf haf, bojíte se mě?")

    def kousej(self):
        print("Ukousnul jsem ti kus nohavice.")



alik1 = Pes("Alík", "vlčák")    
alik2 = Pes("Rex", "bernardýn")
alik3 = Pes("Filip", "jezevčík")

print(alik1.jmeno)
print(alik1.rasa)
alik1.stekej()
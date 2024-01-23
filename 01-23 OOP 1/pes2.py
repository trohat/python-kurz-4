# jdeme vytvořit třídu Pes, což je továrna (vzor) pro výrobu psů
# metoda __init__ je takzvaná dunder metoda, což je zkratka pro "double underscore"

class Pes:
    def __init__(self, jak_se_bude_jmenovat, jakou_bude_mit_rasu):
        self.jmeno = jak_se_bude_jmenovat
        self.rasa = jakou_bude_mit_rasu

    def stekej(self):
        print("Haf haf haf, bojíte se mě?")

    def kousej(self):
        print("Ukousnul jsem ti kus nohavice.")



alik1 = Pes("Alík", "vlčák")    
alik2 = Pes("Rex", "bernardýn")
alik3 = Pes("Filip", "jezevčík")
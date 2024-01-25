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

    def __repr__(self): # tomuhle se říká systémový podpis a má formální pravidla, tedy teď není správně napsaná
        return f"Já jsem pes jménem {self.jmeno}. A tohle vzniklo pomocí dvoupodtržítkové metody repr."    

    def __str__(self): # tomuhle se říká uživatelský podpis a má to být hezky čitelné pro uživatele
        return f"Já jsem pes jménem {self.jmeno}. A tohle vzniklo pomocí dvoupodtržítkové metody str."



alik = Pes("Alík", "vlčák")    
rex = Pes("Rex", "bernardýn")
filip = Pes("Filip", "jezevčík")

print(alik.jmeno)
print(alik.rasa)
alik.stekej()

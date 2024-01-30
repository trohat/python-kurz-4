""" 2.) Vytvořte třídu Kniha. Kniha má jméno, autora a rok vydání.
Vytvořte třídu PoliceNaKnihy. Do police se vejde neomezené množství knih.
Vytvořte ve třídě metodu na přidávání knih (ať je nemusíte přidávat ručně.)

Zařiďte, ať se Kniha i PoliceNaKnihy hezky vypisuje.

Vytvořte několik instancí knih, aspoň jednu instanci PoliceNaKnihy a 
několik knih do ní uložte. """

class Kniha:

    def __init__(self,jmeno_knihy, autor, rok_vydani):
        self.jmeno_knihy = jmeno_knihy
        self.autor = autor
        self.rok_vydani = rok_vydani
    
    def __str__(self):
        return f"řádek 18:\n\t Tato kniha se jmnenuje {self.jmeno_knihy}, od {self.autor} a rok vydání {self.rok_vydani}. "
    
    def __repr__(self):
        return f"řádek 18:\n\t Tato kniha se jmnenuje {self.jmeno_knihy}, od {self.autor} a rok vydání {self.rok_vydani}. "

    """ celkem knih = veškeré knihy na polici """

class PoliceNaKnihy:
    def __init__(self):
        self.celkem_knih = []
        self.pocet_knih = 0
        
    def __str__(self):
         return f"řádek 27: \n\tV polici máme tyto knihy: {self.celkem_knih}" 
        
#pridávám objekt police na knihy kniha
    def pridani_knihy(self,kniha):

        # metoda append - kam = co !
        self.celkem_knih.append(kniha)
        self.pocet_knih += 1

    



# vytvoření knih
kniha1 = Kniha("Staré pověsti české", "Alois Jirásek", 2018)
kniha2 = Kniha("Byl jednou jeden život", "Albert Barielle", 2021)

# vypsání knih
print(kniha1) # vypíše Tato kniha se jmnenuje Staré pověsti české, od Alois Jirásek a rok vydání 2018.
print(kniha2)

# vytvoření police
police1 = PoliceNaKnihy()

#přidávání knih do police
police1.pridani_knihy(kniha1)
police1.pridani_knihy(kniha2)

#tisk police funguje, ale řádek 27 tiskne objekt , né jméno knihy, jak bych chtěl
print(police1)




  


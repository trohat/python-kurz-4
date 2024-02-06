
class Zvire:
    def __init__(self, pocet_koncetin, barva):
        self.pocet_nohou = pocet_koncetin
        self.barva = barva

    def vydej_zvuk(self):
        pass


class Slon(Zvire):
    def __init__(self, barva, delka_chobotu):
        super().__init__(4, barva)
        self.delka_chobotu = delka_chobotu

    def vydej_zvuk(self):
        return "Trůůůů trůůůů trůůů"
    
    def strikej_vodu(self):
        return ("stříkám na lidi kolem sebe")
    
    def __str__(self):
        return f"{self.barva[:-1]}ý {self.__class__.__name__.lower()}"
    

class Opice(Zvire):
    def __init__(self, barva, jmeno, typ_srsti):
        super().__init__(4, barva)
        self.jmeno = jmeno
        self.typ_srsti = typ_srsti

    def vydej_zvuk(self):
        return f"Já jsem opice {self.jmeno}"
    
    def podrbej_se(self):
        return "Drbání mě baví."
    
    def __str__(self):
        return self.jmeno
    

class Had(Zvire):
    def __init__(self, barva, jedovatost):
        super().__init__(0, barva)
        self.jedovatost = jedovatost

    def vydej_zvuk(self):
        return "Sssssssssssssssssssss"
    
    def vyhrivej_se_na_slunicku(self):
        return "Jééé to je krásně teplo."
    
    def __str__(self):
        return f"{self.barva[:-1]}ý {self.__class__.__name__.lower()}"
    

slon1 = Slon("šedá", 2.5)
slon2 = Slon("modrá", 3)
slon3 = Slon("rezavá", 6)

rozarka = Opice("rezavá", "Rozárka", "hodně hustá")
agatka = Opice("hnědá", "Agátka", "jemná")
filip = Opice("černá", "Filip", "krátká")

zmije = Had("šedá", True)
anakonda = Had("zelená", False)
hroznys = Had("žlutá", False)

seznam_zvirat = [slon1, slon2, rozarka, agatka, filip, zmije, anakonda, hroznys]  





for zvire in seznam_zvirat:
    print(zvire.barva)
    print(zvire.vydej_zvuk())



# polymorfismus -> POTOMEK ZASTOUPÍ PŘEDKA
# kód tady v cyklu je psaný pro třídu Zvíře (barva i vydej_zvuk patří zvířeti, ne Hadovi ani Slonovi)    
# ale naprosto v klidu tam místo Zvířete můžeme poslat instanci třídy Opice, Slon nebo Had
# protože Had zastoupí Zvíře
# tedy potomek zastoupí předka



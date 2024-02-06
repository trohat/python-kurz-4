class Zvire:
    def __init__(self, pocet_nohou, barva):
        self.pocet_nohou = pocet_nohou
        self.barva = barva
    
    def vydej_zvuk (self):
        pass
    
class Pes(Zvire):
    def __init__(self,pocet_nohou, barva, rasa):
       Zvire.__init__(self, pocet_nohou, barva)# nebo super().__init__(pocet_nohou, barva)
       self.rasa = rasa 
    
    def __repr__(self):
        return f"{self.rasa}" # definuji co se může vypisovat ve třídě 
    
    def vydej_zvuk (self):
        return f"Dej si na mě pozor {self.rasa} vrrrrr vrrrr"
    
    def hlidej (self):
        return f"Hlídá: {self.rasa}:Jsem hlídací pes! "
    
############################# instance psů #####################################
bernardyn = Pes (4,"hnědá", "bernardýn")  
buldog = Pes (4,"bílá", "buldog")
chrt = Pes (4,"bílá", "chrt")
####################################################################################

class Had(Zvire):
    def __init__(self, barva, druh, jed, skrtic):
        Zvire.__init__(self, 0, barva)
        self.druh = druh 
        self.jed = jed
        self.skrtic = skrtic

    def __repr__(self):
        return f"{self.druh}"
    
    def vydej_zvuk(self):
        return f"{self.druh}: Jsem nebezpečný had SSSSSssssssss"
    
    def utoc(self):
        if self.jed == True:
            return f"jsem {self.druh}, kousnu tě a můj jed tě omámí."
        elif self.skrtic == True:
            return f" Jsem {self.druh}, dej si pozor jsem škrtič."
        else:
            return f"{self.druh} není nebezpečná."
        
############################### instance hadů #######################################
kobra = Had ("černá", "kobra královská", True, False)
uzovka = Had ("šedá", "užovka", False, False)
zmije = Had ("šedá", "zmije", True, False)
krajta = Had("šedá", "krajta královská", False, True)
######################################################################################

class Slon(Zvire):
    def __init__(self, pocet_nohou, barva, vek):
        super().__init__(pocet_nohou, barva)
        self.vek = vek
    
    def __repr__(self):
        return f"Jsem slon ve věku:{self.vek}"
    
    def vydej_zvuk(self):
        return f"Já troubííííímmmmmm Tuuuuu Tuuuuuuu"

    def spi(self):
        return f"Práve jsem usnul"

############################## instance slonů #############################################
tara = Slon(4,"šedá", 32)
shelbi = Slon(4, "hnědá", 60)
yen = Slon (4,"modrá", 12)
#######################################################################################

class Zirafa(Zvire):
    def __init__(self,jmeno, pocet_nohou, barva,):
        super().__init__(pocet_nohou, barva)
        self.jmeno = jmeno
    
    def __repr__(self):
        return f"{self.jmeno}"
    
    def vydej_zvuk(self):
        return f"{self.jmeno}: Já chrochtám jsem žirafa"
    
    def snidam(self):
        return f"Žirafa právě snídá"
    
################################## instance žiraf #######################################
kleopatra = Zirafa("kleopatra", 4, "žlutá s hnědými fleky")
oliver = Zirafa ("Oliver", 4, "žlutá s hnědymi fleky")
jimmy = Zirafa ("Jimmy", 4, "žlutá medová")
#########################################################################################   
##########seznam zvířat, uložení, cyklus, zavolání metody vydej zvuk ####################
seznam_zvirat = [chrt, buldog, uzovka, kobra, tara, yen, kleopatra, jimmy]

for zvire in seznam_zvirat:
    print(zvire.vydej_zvuk())
########################################################################################
###################### třída klec , metoda přidání zvířete ##############################

class Klec:
    def __init__(self):
        self.celkem_zvirat = []  

    def __repr__(self):
        return f"{self.celkem_zvirat}"
     
    def pridej_zvire(self, zvire): 
        if isinstance(zvire, Zvire):
            self.celkem_zvirat.append(zvire)
        else:
            print ("Nelze přidat, není to Zvíře")

##################### instance klecí a umístění zvířat - zavolání metody ###############

klec_na_zvirata1 = Klec()
klec_na_zvirata1.pridej_zvire(chrt)
klec_na_zvirata1.pridej_zvire(kobra)
klec_na_zvirata1.pridej_zvire(bernardyn)
print(f"\n\tVypisuji seznam zvířat v kleci 1:{klec_na_zvirata1}")

klec_na_zvirata2 = Klec()
klec_na_zvirata2.pridej_zvire(buldog)
klec_na_zvirata2.pridej_zvire(uzovka)
klec_na_zvirata2.pridej_zvire(tara)
klec_na_zvirata2.pridej_zvire(shelbi)
print(f"\n\tVypisuji seznam zvířat v kleci 2:{klec_na_zvirata2}")
print("################################################################################")
print("###############           zakládám ZOO             ##############################")
print("#################################################################################")
##########################################################################################

class Zoo:
    # třídní atribut je sdílen mezi všemi instancemi ve třídě Zoo  
    pocet_kleci = 0
    seznam_zvirat_v_kleci = []
    seznam_nohou = 0
    seznam_podle_barvy = []
    seznam_podle_nohou = []
    
    #výpis klecí v Zoo a zvířata v něm
    def __repr__(self):
        return f" V Zoo máme celkem tyto klece:{Zoo.seznam_zvirat_v_kleci}"
    
    def pridej_klec(self, klec):
        Zoo.seznam_zvirat_v_kleci.append(klec)
        Zoo.pocet_kleci += 1 
        return Zoo.pocet_kleci 
    
    def vypis_podle_barvy(self, barva):
        for i in Zoo.seznam_zvirat_v_kleci: # procházím klec v seznamu klecí
            for zvire in i.celkem_zvirat: # procházím zvíře v kleci
                if zvire.barva == barva:
                    Zoo.seznam_podle_barvy.append(zvire)
        return f" {barva} barva patří těmto zvířatům v Zoo: {Zoo.seznam_podle_barvy} "
    
    def vypis_podle_nohou(self, pocet_nohou):
        for klec in Zoo.seznam_zvirat_v_kleci:
            for zvire in klec.celkem_zvirat:
                if zvire.pocet_nohou == pocet_nohou:
                    Zoo.seznam_podle_nohou.append(zvire)
        return f"V zoo máme ty zvířata se {pocet_nohou} nohy {Zoo.seznam_podle_nohou}"
    
    def spocitej_nohy(self):
        for klec in Zoo.seznam_zvirat_v_kleci: 
            for zvire in klec.celkem_zvirat: 
                Zoo.seznam_nohou += zvire.pocet_nohou
        return f"V Zoo máme celkem {Zoo.seznam_nohou} nohou."
  
############################instance klecí a volání metody ##############################
klec_do_zoo1 = Zoo()
klec_do_zoo2 = Zoo()
klec_do_zoo1.pridej_klec(klec_na_zvirata1)
klec_do_zoo2.pridej_klec(klec_na_zvirata2)

print("vypisuji klec1 v zoo")
print(klec_do_zoo1)
print("vypisuji klec2 v zoo")
print(klec_do_zoo2)

###############################instance Zoo přidání dvou klecí vypsání  ##################################################
zoo = Zoo()
zoo.pridej_klec(klec_na_zvirata1)
zoo.pridej_klec(klec_na_zvirata2)

print(f"\n\tZoo má celkem {zoo.pocet_kleci} klece.")
# výpis zvířat s šedou barvou
print("\n\t\t\tvypisuji zvířata v kleci  podle barvy:")
barva_ke_hledani = "šedá"
print(zoo.vypis_podle_barvy(barva_ke_hledani))
# výpis zvířat s nohami
nohy_ke_hledaní = 4
print(zoo.vypis_podle_nohou(nohy_ke_hledaní))
# výpis nohou celkem v Zoo
print(zoo.spocitej_nohy())

   






    
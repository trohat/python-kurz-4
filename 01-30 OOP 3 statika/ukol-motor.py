class Motor:
    def __init__(self, typ, vykon):
        self.typ = typ
        self.vykon = vykon

    def __str__(self):
        return f"Jsem motor typu: {self.typ} a vykonu: {self.vykon}"
    
class Auto:
    def __init__(self, znacka, motor, akt_stav_benzinu, max_benzinu):
        self.znacka = znacka
        self.motor = motor
        self.akt_stav_benzinu = akt_stav_benzinu
        self.max_benzinu = max_benzinu

    """ spotřeba benzínu je celková spotřeba benzínu za výlet """
    def jet_na_vylet(self, cil_vyletu, spotreba_benzinu,stav_peněženky):
        #self.cil_vyletu = cil_vyletu
        #self.spoteba_benzinu = spotreba_benzinu
        if spotreba_benzinu <= self.akt_stav_benzinu: # spotreba benzinu jako lokální proměnná, nemusím použít self.spotreba benzinu
            print(f" Vyrážíme na vylet do: {cil_vyletu} ")
        else:
            print(f"Musíme natankovat, stav peněženky = {stav_peněženky}")
            return 
        
        print(f"Auto značky {self.znacka} jede na výlet.")
        self.akt_stav_benzinu = self.akt_stav_benzinu - spotreba_benzinu
        #self.stav_penezenky = stav_peněženky 
        

        """ podmínka pokud je cíl výletu < než spotřeba , jede se na výlet pokud ne musíme
         natankovat """
        
        
    def __str__(self):
        return f"Já jsem auto značky: {self.znacka}  motoru:{self.motor} stav benzinu {self.akt_stav_benzinu}"
    
       
 ###################################################################################
motor_skoda = Motor("benzin",1.8) # instance Motoru
auto_skoda = Auto("skoda", motor_skoda,40,80)

print(auto_skoda)
print(motor_skoda)

#vytvoření několik instancí motoru
motor_tesla = Motor("elektrický", 1.2)
motor_citroen = Motor("hybrid", 1.5)
motor_bmw = Motor("nafta", 3)

print(f"řádek: 27\n\t{motor_tesla} {motor_citroen} {motor_bmw}")

#vytvoření několik instancí auta (motory z proměnných)
auto_tesla = Auto("Tesla", motor_tesla,20,60) 
auto_citroen = Auto("Citroen", motor_citroen,10,80)
auto_bmw = Auto("BMW", motor_bmw,50,60)

print(f"řádek 34: \n\t{auto_tesla} {auto_citroen} {auto_bmw}")

# motor vytvořený při vytvoření auta
auto_peugeot = Auto("Peugeot", akt_stav_benzinu=20, max_benzinu=60, motor=Motor("benzin",1.2))

print(f"řádek 39:\n\t{auto_peugeot}")

#změna motoru přes auto 

auto_bmw.motor = Motor("benzin", 2.5)
print(f"změna motoru, řádek 44:\n\t{auto_bmw}")
    
    #metoda výletu: parametry : cíl výletu, spotřeba benzínu, stav peněženky
auto_skoda.jet_na_vylet("Praha",30,80)  

print(auto_skoda)



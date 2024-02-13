# hraní si s private proměnnými, též pokročilá látka

class Pes:
    def __init__(self, jmeno, rasa):
        self.jmeno = jmeno
        self.__rasa = rasa

    def _stekej(self):
        print("Haf haf haf")

    def __kousej(self):
        print("Vrrrrr haf")

    def zkus_volat_private_veci(self):
        self.__kousej()
        print(self.__rasa)
    
    @property
    def jmeno(self):  # get_jmeno
        return self._jmeno
    
    @jmeno.setter
    def jmeno(self, value): # set_jmeno
        print("setter called")
        self._jmeno = value



pes = Pes("Alík", "vlčák")
pes.jmeno= "Blbec"
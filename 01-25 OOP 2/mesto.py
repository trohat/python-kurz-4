from clovek import adam, bedrich, kamil, Clovek
from auto import auto1, auto2, auto3, Auto

# menší úprava oproti realitě, v každém městě bydlí jen jeden člověk, vylepšíme příště
class Mesto:
    def __init__(self, jmeno, clovek):
        self.jmeno = jmeno
        self.clovek = clovek

mesto1 = Mesto("Praha", adam)
mesto2 = Mesto("Brno", kamil)
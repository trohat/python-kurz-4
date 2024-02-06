
from abc import ABC, abstractmethod

class Zvire(ABC):
    def __init__(self, pocet_nohou, barva):
        self.pocet_nohou = pocet_nohou
        self.barva = barva

    @abstractmethod
    def vydej_zvuk(self):
        pass



slon = Zvire(4, "šedá") # NEJDE!!!! lze jen dědit
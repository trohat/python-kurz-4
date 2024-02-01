# abstraktní třídy a metody, pokročilá látka

from abc import ABC, abstractmethod

class Zamestnanec(ABC):
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    @abstractmethod
    def pracuj(self):
        pass


class Programator(Zamestnanec):
    def pracuj(self):
        print("Vymyslel jsem novou aplikaci.")

class KdoDelaMarketing(Zamestnanec):
    def pracuj(self):
        print("Získal jsem nového zákazníka.")

class Grafik(Zamestnanec):
    def pracuj(self):
        print("Vyrobil jsem krásnou šablonu.")


pepa = Programator("Josef", "Dvořák")

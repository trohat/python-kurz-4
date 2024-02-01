

class Pes:
    # Třídní atribut pro sledování počtu vytvořených psů
    pocet_psu = 0

    def __init__(self, jmeno, vek):
        # Instanční atribut pro jméno a věk psa
        self.jmeno = jmeno
        self.vek = vek
        # Inkrementace třídního atributu při vytvoření nového instance psa
        Pes.pocet_psu += 1

# Příklad použití třídy Pes
pes1 = Pes("Max", 3)
pes2 = Pes("Buddy", 2)

# Vypsání počtu vytvořených psů
print("Celkový počet psů:", Pes.pocet_psu)

#=======================


class Pes:
    # Třídní proměnná pro sledování počtu vytvořených psů
    pocet_psu = 0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        # Při vytvoření instance zvýšíme počet_psu o 1
        Pes.pocet_psu += 1

# Vytvoření několika instancí Pes
pes1 = Pes("Buddy")
pes2 = Pes("Max")
pes3 = Pes("Luna")

# Výpis počtu vytvořených psů
print(f"Celkový počet psů: {Pes.pocet_psu}")

#====================


class Pes:
    pocet_psu = 0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        Pes.pocet_psu += 1

    def vypis_pocet_psu_instancne(self):
        print(f"Celkový počet psů (instancní metoda): {self.__class__.pocet_psu}")

    @staticmethod
    def vypis_pocet_psu_staticky():
        print(f"Celkový počet psů (statická metoda): {Pes.pocet_psu}")

    @classmethod
    def vypis_pocet_psu_tridne(cls):
        print(f"Celkový počet psů (třídní metoda): {cls.pocet_psu}")


# Vytvoření několika instancí Pes
pes1 = Pes("Buddy")
pes2 = Pes("Max")

# Volání instanční metody
pes1.vypis_pocet_psu_instancne()

# Volání statické metody na úrovni třídy
Pes.vypis_pocet_psu_staticky()

# Volání třídní metody na úrovni třídy
Pes.vypis_pocet_psu_tridne()

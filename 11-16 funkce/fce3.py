
def prijmy(prijem1, prijem2, prijem3):
    celkovy_prijem = prijem1 + prijem2 + prijem3
    return celkovy_prijem

def vydaje(vydaj1, vydaj2, vydaj3):
    celkove_vydaje = vydaj1 + vydaj2 + vydaj3
    return celkove_vydaje

def dan(prijmy, vydaje, sazba):
    celkova_dan = (prijmy - vydaje) * sazba // 100
    return celkova_dan

moje_prijmy = prijmy(50000, 60000, 2000)

moje_vydaje = vydaje(500, 8000, 700)

moje_dan = dan(moje_prijmy, moje_vydaje, 15)

print(f"Letos platíš daň {moje_dan} Kč.")
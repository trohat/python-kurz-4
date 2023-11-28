import random

def vytvor_seznam(delka, dolni_hranice, horni_hranice):  
    ''' vytvoří seznam celých čísel, o počtu prvků delka, od čísla dolni_hranice
    do čísla horni_hranice, včetně obou z nich '''
    seznam_cisel = []
    for i in range(delka):
        cislo = random.randrange(dolni_hranice, horni_hranice + 1)
        while cislo in seznam_cisel:
            cislo = random.randrange(dolni_hranice, horni_hranice + 1)
        seznam_cisel.append(cislo)
        #print(seznam_cisel)
    return seznam_cisel

muj_seznam = vytvor_seznam(6, -20, 20)

print(muj_seznam)

soucet_zapornych = 0
soucet_sudych = 0

for cislo in muj_seznam:
    if cislo < 0:
        soucet_zapornych += cislo
    if cislo % 2 == 0:
        soucet_sudych += cislo

print(f"Součet záporných čísel v seznamu je {soucet_zapornych}.")
print(f"Součet sudých čísel v seznamu je {soucet_sudych}.")





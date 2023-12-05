cislo = 5
cislo2 = cislo

cislo2 = 7
cislo = 4

slovnik1 = {"slon":"elephant", "opice":"monkey"}
slovnik2 = slovnik1
pomocna_sipka = slovnik1

slovnik2["lev"] = "lion"

slovnik2 = {"slon":"elephant", "opice":"monkey"}
slovnik1 = slovnik2

def pridej_do_slovniku_hada(sl):
    sl["had"] = "snake"
    return sl
    
pridej_do_slovniku_hada(slovnik1)
print(slovnik2)
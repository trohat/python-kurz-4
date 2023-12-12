slovnik1 = {
    "slon":"elephant", 
    "opice":"monkey"
}

def pridej_do_slovniku_hada(sl, cislo2):
    cislo1 = 12
    cislo2 += 3
    sl["had"] = "snake"
    return sl
    

cislo2 = 5
pridej_do_slovniku_hada(slovnik1, cislo2)
print(slovnik1)
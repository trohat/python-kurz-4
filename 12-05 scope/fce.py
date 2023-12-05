
def scitani(cislo1):
    global cislo2
    vysledek = cislo1 + cislo2
    cislo2 += 5
    print(f"Jsem uvnitř funkce, číslo2 = {cislo2}")


cislo1 = 23

cislo2 = 45


print(scitani(cislo1))

print(f"Jsem mimo funkci, číslo2 = {cislo2}")
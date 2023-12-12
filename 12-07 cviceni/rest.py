
menu_v_restauraci = {
    "knedlo vepřo zelo": 120,
    "rizoto": 100,
    "kachna s knedlíkem": 180,
    "tlačenka": 90,
    "plněné knedlíky uzeným masem": 180,
    "ovocné knedlíky": 120,
}

def seznam_pprint(seznam):
    print("Běžím, teď!")
    if len(seznam) == 0:
        return ""
    vysledek = "\n"
    for polozka in seznam:
        vysledek += polozka.rjust(30) + ", "
    return vysledek

    

print("\n\n Toto je program v retauraci")
def objednavka(menu):
    celkova_objednavka = []
    celkova_cena = 0

    while True:
        vybrane_jidlo = input(f"Jaké jídlo jste si vybral z naší nabídky? (pro ukončení stiskněte Enter) ")
        if vybrane_jidlo == "":
            break
        elif vybrane_jidlo in menu:
            celkova_objednavka.append(vybrane_jidlo)
            celkova_cena += menu[vybrane_jidlo]
            print(f"\npotvrzujeme vaši objednávku {seznam_pprint(celkova_objednavka)}")
        else:
            print("Omlouváme se toto jídlo nemáme v nabídce, vyberte si jiné")
    
    if celkova_objednavka:
        print(f"\nDěkujeme za objednávku:{seznam_pprint(celkova_objednavka)} \ncelková cena:{celkova_cena} Kč")

objednavka(menu_v_restauraci)

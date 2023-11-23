# krásně vypracovaný úkol od Aničky, plus pár malých úprav ode mne
# místo kapel jsou zvířata

#1.) Vytvořte seznam, ve kterém bude šest vašich oblíbených kapel.

zvire = ["kocka", "pes", "slon", "mys", "klokan", "veverka"]
print(zvire)

#2.) Vypište kapelu na druhém a čtvrtém místě.

print(f"zvire na druhem miste je ", zvire[1])
print(f"zvire na druhem miste je ", zvire[3])


#3.) Rozmysleli ste si to. Vaše nejoblíbenější kapela (tedy ta na prvním místě)
#se změnila. Změňte odpovídajícím způsobem seznam.
zvire[0] = "jiná opice"
print(f"novy seznam ", zvire)

#4.) Přidejte do seznamu sedmou a osmou kapelu.
zvire.append("had")
zvire.append("papousek")
print(f"doplneny seznam o 7 a 8 zvire ", zvire)

#5.) Vytvořte nový seznam (pomocí list slicing), kde budou kapely od indexu 1
#do indexu 5.

novy_zvire = zvire[1:6]
print(f"seznam zvire od 1 do 5", novy_zvire)

#5b.) Pomocí list slicing vytvořte seznam s kapelami od druhého místa až do konce 
#seznamu.
novy_zvire = zvire[1:]
print(f"zvire od 2 do konce", novy_zvire)

#5c.) To samé, ale kapely od začátku až do třetí pozice.

novy_zvire = zvire[:4]
print(f"zvire od začátku až do třetí pozice.", novy_zvire)

#5d.) To samé, ale jen první, třetí a pátou kapelu.

novy_zvire = zvire[1:6:2]
print(f"zvire jen první, třetí a páte", novy_zvire)

#5e.) Vytvořte pomocí list slicing kopii celého seznamu.

kopie_zvire = zvire[:]
print(f"kopie celeho seznamu ", kopie_zvire)

#5f.) Vytvořte pomocí list slicing kopii celého seznamu, ale řazenou pozpátku.

kopie_zvire_pozpatku = zvire[::-1]
print(kopie_zvire_pozpatku)

#6.) Vzpomeňte si na jednu z kapel v seznamu a pomocí Pythonu zjistěte, na 
#kolikáté je pozici.

misto_opice = zvire.index("opice")
print(f"opice je na miste cislo ", misto_opice)


#7.) Nemáte tam nějakou kapelu 2x? Vyberte jednu náhodnou a zjistěte, kolikrát se 
#v seznamu vyskytuje.

vybrane_zvire = "veverka"
pocet = zvire.count(vybrane_zvire)
print(f"zvire '{vybrane_zvire}' je uvedena {pocet} krat")

#8.) Na třetí pozici vložte jinou kapelu (tu, co byla původně třetí ale nevymažte, 
#jen ať se posune na 4té místo.)


zvire.insert(2, "tucniak")
print(f"Novy seznam zvire ", zvire)

#9.) Odeberte ze seznamu kapelu na páté pozici.

del zvire[5]
print(f"po odebrani 5 zvire seznam je ", zvire)

#10.) Vypište délku seznamu.

delka = len(zvire)
print(f"delka seznamu {delka} zvire")

#11.) Vypište seznam s kapelami, a to tak že se na každém řádku vypíše:
#"Moje nej kapela na x. místě je jméno-kapely." (Místo x a jména bude
#skutečné číslo a jméno.)


zvire = ["kocka", "pes", "slon", "mys", "klokan", "veverka"]
print(zvire)
for i, zvire in  enumerate(zvire, start=1):
    print(f"Moje nej zvire na {i}.miste je {zvire}")

print('\n')

#12.) Udělejte si seznam, kde bude přibližně deset různých čísel. Pomocí funkcí v Pythonu
#zjistěte, jaké je z nich největší, jaké je nejmenší a kolik je jejich součet.

cisla = [5, 12,32, 8, 55, 66, 14, 99, 3, 17]
print(cisla)

celkem = sum(cisla)
max = max(cisla)
min = min(cisla)
print(f"soucet cisel je ", celkem,"," "maximalne cislo je ", max,"," "minimalne cislo je ", min)


#13.) To samé jako úkol 12, ale máte zakázáno používat funkce max, min a sum (tedy, musíte si
#to naprogramovat sami.)

cisla = [5, 12,32, 8, 55, 66, 14, 99, 3, 17]
print(cisla)

max = cisla[0]
for cislo in cisla:
    if cislo > max:
        max = cislo
print(f"najvetsi cislo je ", max)

min = cisla[0]
for cislo in cisla:
   if cislo < min:
       min = cislo
print(F"nejmensi cislo je ", min)

celkem = cisla[0]
for cislo in cisla:
   celkem += cislo
print(f"soucet cisel ", celkem)

#14.) Projděte seznam s čísly a vypočítejte průměr čísel v seznamu. 

prumer = sum(cisla) / len(cisla)
print(f"prumer cisel je", prumer)
from pprint import pprint
print = pprint

#0.) Vytvořte slovník, který odpovídá slovníku pro překlad do nějakého cizího jazyka.
#(např. slovíčka v češtině a ve francouzštině - zvolte si jazyk, který umíte)
slovnik = {
    "jmeno": "name",
    "ruka": "hend",
    "oko": "eye",
    "mladý": "young",
    "velký": "big",
    "ucho": "ear",
}

slovnik["noha"] = "food"
slovnik["židle"] = "chair"
pprint(f" Do slovníku jsou přidána noha a židle{slovnik}")
# změna překladu slovíčka
slovnik["jmeno"] = "blbost"
blbost = slovnik["jmeno"]
print("řádek 20:", f"Tisk překladu jméno je: {blbost}")

# První sada:
# restaurace
# a)
restaurace = {
    "svíčková": 150,
    "knedlo vepřo zelo": 145,
    "kachna se zelím s knedlíkem": 230,
}

#b) přidání 
restaurace["bramborák"] = 70
restaurace["zmrzlinový pohár"] = 90

#c) změna ceny
restaurace["svíčkova"] = 170
print("\n\nsvíčková - změna ceny")
pprint(restaurace)

#d) vymazání

del restaurace["bramborák"]
print(restaurace)

#2.) Napište funkci, která vypíše všechna jídla
#(lehčí varianta: nemusí to být funkce, vypište je jen tak)
print("\n\ntisknu položky slovníku")
for i in restaurace.keys():
    print(i) 


def scitani(cislo1, cislo2):
    vysledek = cislo1 + cislo2
    print(vysledek)
    print("Zvracení na ulici")
    return None

def jidla(menu):
    for i in menu.keys():
        print(i)

jidla(restaurace)

print(scitani(3, 5))


#3.) Napište funkci, která vypíše celé menu - tj. jídla i s cenami
#(též můžete zvolit lehčí variantu bez funkce)
"""
def cele_menu():
    for i in restaurace.items():
        print(i)
cele_menu()

# 4.) Napište funkci, která si vezme od hosta objednávku a připraví mu účet.Host bude postupně 
# zadávat jídla, která si chce dát (pomocí inputu).Pokud jídlo máme v menu, tak se vypíše 
# potvrzení a cena (host si samozřejmě může objednat stejné jídlo vícekrát)
# Pokud jídlo nemáme, tak se vypíše "omlouváme se zrovna došlo" nebo takovou blbost jsme 
# nikdy neměli" (záleží na vás jak hodní chcet být na hosty)Pokud host zadá prázdný řetězec, 
# znamená to, že skončil s objednáváním a vypíše se celková cena.

menu = {
    "knedlo vepřo zelo": 120,
    "rizoto": 100,
    "kachna s knedlíkem": 180,
    "tlačenka": 90,
    "plněné knedlíky uzeným masem": 180,
    "ovocné knedlíky": 120,
}

print("Toto je program v retauraci")
def objednavka(menu):
    vybrane_jidlo = input(f"Jaké jídlo jste si vybral z naší nabídky?")
    if vybrane_jidlo in menu:
        print(f"potvrzujeme vaši objednávku {vybrane_jidlo}")
    else:
        print("Omlouváme se toto jídlo nemáme v nabídce, vyberte si jiné")
objednavka(menu)










"""
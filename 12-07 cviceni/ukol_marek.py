from pprint import pprint
#0.) Vytvořte slovník, který odpovídá slovníku pro překlad do nějakého cizího jazyka.
#(např. slovíčka v češtině a ve francouzštině - zvolte si jazyk, který umíte)
slovnik = {
    "jmeno": "name",
    "ruka": "hend",
    "oko": "eye",
    "mladý": "young",
    "velký": "big",
}

slovnik["noha"] = "foot"
slovnik["židle"] = "chair"
print(f" Do slovníku jsou přidána noha a židle{slovnik}")
# změna překladu slovíčka
slovnik["jmeno"] = "blbost"
blbost = slovnik["jmeno"]
print(f" 18 Tisk překladu jméno je: {blbost}")

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
restaurace["svíčková"] = 170
pprint(f"35 {restaurace}")

#d) vymazání

del restaurace["bramborák"]
pprint(restaurace)

#2.) Napište funkci, která vypíše všechna jídla
#(lehčí varianta: nemusí to být funkce, vypište je jen tak)
"""     for i in restaurace.keys():
        print(i) """

def jidla(menu):
    for i in menu.keys():
        print(i)
jidla(restaurace)

#3.) Napište funkci, která vypíše celé menu - tj. jídla i s cenami
#(též můžete zvolit lehčí variantu bez funkce)

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

menu_v_restauraci = {
    "knedlo vepřo zelo": 120,
    "rizoto": 100,
    "kachna s knedlíkem": 180,
    "tlačenka": 90,
    "plněné knedlíky uzeným masem": 180,
    "ovocné knedlíky": 120,
}

print("\n\n Toto je program v retauraci")
def objednavka(menu):
    celkova_objednavka = []
    celkova_cena = 0

    while True:
        vybrane_jidlo = input(f"Jaké jídlo jste si vybral z naší nabídky?")
        if vybrane_jidlo == "":
            break
        elif vybrane_jidlo in menu:
            celkova_objednavka.append(vybrane_jidlo)
            celkova_cena += menu[vybrane_jidlo]
            print(f"\npotvrzujeme vaši objednávku {celkova_objednavka}")
        else:
            print("Omlouváme se toto jídlo nemáme v nabídce, vyberte si jiné")
    
    if celkova_objednavka:
        print(f"\nDěkujeme za objednávku:{celkova_objednavka} \ncelková cena:{celkova_cena} Kč")

objednavka(menu_v_restauraci)

#5.) Vytvořte slovník, kde klíče jsou uživatelská jména a hodnoty jsou
# hesla. Zeptejte se uživatele na jméno a heslo a sdělte mu,
# jestli se úspěšně přihlásil.
# (POZOR - v praxi nikdy neukládejte hesla tímto způsobem, toto je jen 
# cvičení. Hesla musí být skrytá, zakódovaná.)

uzivatelske_prihlaseni = {
    "Rafael Nadal" : "levá_ruka",
    "Karel Erben" : "Kytice",
    "Bohdan Ulihrach" :"smolař2023",
}

def prihlaseni(jmeno,heslo):
    while True:
        if jmeno in uzivatelske_prihlaseni and heslo == uzivatelske_prihlaseni[jmeno]:
            print("Přihlášení bylo úspěšné")
        else:
            print("přihlášení se nezdařilo")


prihlaseni(jmeno, heslo)  

#6.) Definujte slovník, kde klíče jsou data v příštím týdnu (vyjádřená 
# stringem nebo ještě lépe jen jedním číslem) a hodnoty jsou 
# teploty v dané dny.Těžší verze: Hodnoty jsou další slovníky, kde je uložena 
# nejen teplota, ale i slovní popis počasí a rosný bod. 
# Po zadání data program vypíše, jak bude, případně jak bude den potom a dva dny potom.
    
predpoved = {
    "pondělí" : {
        "teplota": 20,
        "popis": "slunečno",
        "rosný bod": 10
        },
    "úterý": {
        "teplota": 21,
        "popis": "slunečno",
        "rosný bod": 12
        },
    "středa": {
        "teplota": 13,
        "popis": "zataženo",
        "rosný bod": 10
        },
    "čtvrtek": {
        "teplota": 18,
        "popis": "zataženo a místy přeháňky",
        "rosný bod": 12
        },
    "pátek":{
        "teplota": 22,
        "popis": "slunečno",
        "rosný bod": 13
        },
    "sobota": {
        "teplota": 18,
        "popis": "místy přeháňky",
        "rosný bod": 12
        },
    "neděle": {
        "teplota": 22,
        "popis": "slunečno",
        "rosný bod": 12
        },
}

print("\n Program na vypsání předpovědi")
def program_predpoved():
    den = input("Pro jaký den chceš vypsat předpověď?")

    if den in predpoved:
        print(f"\n Předpověď pro den: {den}")
        print(f"Teplota bude: {predpoved[den]['teplota']} °C")
        print(f"V danný den bude: {predpoved[den]['popis']}")
        print(f"Rosný bod bude: {predpoved[den]['rosný bod']}")

    else:print("\nNezadal jsi správný formát pro den napiš v rozmezí pondělí - neděle")
program_predpoved()


        
        












import math
import random

print(' ========================================================  ')
print(' 0a.) Vytvořte si seznam s čísly. Vytvořte nový seznam, kde jsou všechna')
print(' čísla zvětšená o tři. (Můžete pomocí cyklu, později určitě pomocí list')
print(' comprehension.')

# seznamcisel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
seznamcisel = []
for _ in range(20):
    seznamcisel += [random.randint(0, 50)]


# [random.randint(0, 50) for _ in range(20)] 
    
seznamciselplus3 = []

for cislo in seznamcisel:
    seznamciselplus3 += [cislo + 3]

print(seznamcisel)
print(seznamciselplus3)

print(' ')
print(' ========================================================  ')
print(' 0b.) To samé jako 0a, ale lichá čísla z nového seznamu vypadnou.')

seznamciselsuda = []
for cislo in seznamciselplus3:
    if (cislo % 2 == 0):
        seznamciselsuda += [cislo]

print(seznamciselplus3)
print(seznamciselsuda)

print(' ')
print(' ========================================================  ')
print(' 0c.) Vytvořte si seznam se slovy. Vytvořte nový seznam, kde jsou všechna')
print(' slova napsaná velkými písmeny. (Můžete pomocí cyklu, později určitě pomocí list')
print(' comprehension.)')

slova = "vytvořte si seznam se slovy Vytvořte nový seznam kde jsou všechna slova napsaná velkými písmeny".split(
    " ")

print(slova)

UpperSlova = [slovo.upper() for slovo in slova]
print(UpperSlova)

print(' ')
print(' ========================================================  ')
print(' 0d.) To samé jako 0c, ale v novém seznamu budou jen slova delší než tři písmena.')

Len3Slova = [slovo.upper() for slovo in slova if len(slovo) > 3]
print(Len3Slova)

print(' ')
print(' ========================================================  ')
print('# 1.) Napište funkci, která vrátí seznam s třetími mocninami všech čísel')
print('# v zadaném seznamu.')


def tretimocnina(cisla):
    seznamciselmocnina3 = []
    for cislo in seznamcisel:
        seznamciselmocnina3 += [cislo**3]

    return seznamciselmocnina3

print(seznamcisel)
print(tretimocnina(seznamcisel))


print(' ')
print(' ========================================================  ')
print('# 2.) Vytvořte funkci, která vezme seznam čísel (list of ints) a')
print('# vytvoří z nich řetězce.')

seznamciselstr = []
for cislo in seznamcisel:
    seznamciselstr += [str(cislo)]
print(seznamcisel)
print(seznamciselstr)

print(' ')
print(' ========================================================  ')
print('# 2b.) Vytvoří řetězce jen z těch čísel, co jsou menší než 15.')

cislamensi15 = [str(cislo) for cislo in seznamcisel if cislo < 15]
print(seznamcisel)
print(cislamensi15)

print(' ')
print(' ========================================================  ')
print(' 3.) Napište funkci, která vezme řetězec, kde jsou čísla a')
print(' shluky písmenek oddělená mezerami. Funkce vrátí součet čísel')
print(' a písmenka ignoruje.')
print(" příklad: '10 abc 20 de44 30 55fg 40' -> 100")


def sumNumber(radek):
    sum = 0

    for x in radek.split():
        if (x.isnumeric()):
            sum += int(x)

    return sum

radek = '10 abc 20 de44 30 55fg 40'
sum(int(x) for x in radek.split() if x.isnumeric())

print(sumNumber('10 abc 20 de44 30 55fg 40'))

print(' ')
print(' ========================================================  ')
print(' 4.) Vytvořte funkci, která narovná seznam - tj. ze seznamu')
print(' dvě úrovně hlubokého vytvoří seznam jednoúrovňový.')
print(' [[1,2], [3,4]] => [1, 2, 3, 4]')
print(' Asi budete potřebovat vnořený cyklus - v list comprehensions')
print(' lze vnořovat také.')

seznam2 = [[1, 2], [3, 4]]
seznam2u = [cislo for radek in seznam2 for cislo in radek]
print(seznam2u)

print(' ')
print(' ========================================================  ')
print(' 5.) Otočte slovník (pokud jsme už probrali dict comprehensions):')
print(' Vytvořte funkci, která vezme slovník a vytvoří nový slovník,')
print(' kde klíče jsou to, co bylo minule hodnoty a naopak')

CzechToEng = {
    "dřevo": "wood",
    "les": "forest",
    "ovce": "sheep",
    "jablko": "apple",
    "pes": "dog"
}

EngToCzech = {}
EngToCzech.update({e: c for (c, e) in CzechToEng.items()})

print(CzechToEng)
print(EngToCzech)

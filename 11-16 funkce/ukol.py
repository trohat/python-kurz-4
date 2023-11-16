# Develop a game Guess the Number. The program chooses #
# a number in the range from 1 to 500. The user tries to guess it. #
# After each try, the program gives hints on whether the number is greater #
# or less than the guessed number. In the end, the #
# program displays statistics: how many tries it took to guess #
# the number, how long it took. Provide an exit by entering 0 if #
# the user is tired of guessing the number. #

import random

MINRANGE = 1
MAXRANGE = 500

hledane_cislo = random.randrange(MINRANGE, MAXRANGE)

# print(hledane_cislo)

ukoncit = False

while not ukoncit:
    print('----------------------------------------------------------------------------------------') #odradkovani
    cislos = input(
        f'Zkus uhodnout vygenerované číslo (celočíselné) v rozmezí od {MINRANGE} do {MAXRANGE} :')

    if not cislos.isnumeric():
        print('Zadany udaj neni cislo !!!!!')
    else:
        cislo = int(cislos)
        if cislo == 0:
            print(f"Vygenerované číslo je {hledane_cislo}")
            ukoncit = True
        elif (cislo < MINRANGE) or (cislo > MAXRANGE):
            print(f'Zadané číslo není v rozmezí od {MINRANGE} do {MAXRANGE} !!!!!')
        else:
            if hledane_cislo > cislo:
                print('Vygenerované číslo je vyšší než zadané číslo')
            elif hledane_cislo < cislo:
                print('Vygenerované číslo je nižší než zadané číslo')
            else:
                print("Uhodnuto")
                ukoncit = True
            

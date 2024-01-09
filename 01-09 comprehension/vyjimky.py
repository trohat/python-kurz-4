print("program pro dělení dvou čísel")

try:
    cislo1 = int(input("První číslo je: "))
    cislo2 = int(input("Druhé číslo je: "))

    vysledek = cislo1 / cislo2
    print(vysledek) 

except Exception as e:
    print("Nastala neočekávaná chyba")



print("Program vesele pokračuje dál")
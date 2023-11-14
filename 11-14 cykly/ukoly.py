""" Uživatel zadává číslo od 1 do 100. Pokud je toto číslo násobkem 3 
(dělitelné 3 bez zbytku), vypište slovo "Fizz". Pokud je číslo násobkem 5, 
vypište slovo "Buzz". Pokud je číslo násobkem 3 a 5 současně, vypište "Fizz Buzz". 
Pokud číslo není násobkem 3 ani 5, vypište číslo.
Pokud uživatel zadá číslo mimo daný rozsah, vypište chybovou zprávu. """

print("Program Fizz Buzz")

# numberN = int(input("Zadej číslo 1-100."))
numberN = 0
while numberN < 100:
    numberN += 1
    string = ""
    if numberN % 3 == 0:
        string = string + "Fizz"
    if numberN % 5 == 0:
        string = string + "Buzz"
    if string == "":
        print(numberN)
    else:
        print(string)
    
    


if 2 + 3 > 4 * 6

vowels = "aeiouy"

def pig_latin_word(word):
    word = word.lower()   
    first_letter = word[0] 
    if first_letter in vowels:   
        return word + "way"
    return word[1:] + first_letter + "ay"


# print(pig_latin_word("air") == "airway")
# print(pig_latin_word("ear") == "earway")
# print(pig_latin_word("elephant") == "elephantway")
# print(pig_latin_word("cat") == "atcay")
# print(pig_latin_word("papaya") == "apayapay")
# print(pig_latin_word("Computer"))
# print(pig_latin_word("Elephant"))

def pig_latin_s_inputem():  
    slovo = input("Zadej slovo k překladu: ")
    vysledek = pig_latin_word(slovo)
    print(f"Překlad slova {slovo} do tajného jazyka je {vysledek}")

def pig_latin_s_inputem_na_jeden_radek():
    print(f"Výsledek překladu je {pig_latin_word(input('Zadej slovo k překladu: '))}")   

def pig_latin_with_capital(word):
    first_letter = word[0]
    word = pig_latin_word(word)
    if first_letter.isupper():
        return word.title()
    else:
        return word   
    
def pig_latin_with_interpunction(word):
    last_letter = word[-1]
    if last_letter in ".,?!":
        word = word[:-1]
    else:
        last_letter = ""
    word = pig_latin_with_capital(word)
    return word + last_letter


# print(pig_latin_word("Computer") == "omputercay")
# print(pig_latin_with_capital("Computer") == "Omputercay")
# print(pig_latin_with_capital("Elephant") == "Elephantway")
# print(pig_latin_with_capital("elephant") == "elephantway")
print(pig_latin_with_interpunction("elephant") == "elephantway")
print(pig_latin_with_interpunction("elephant,") == "elephantway,")
print(pig_latin_with_interpunction("Elephant,") == "Elephantway,")
print(pig_latin_with_interpunction("Elephant.") == "Elephantway.")
print(pig_latin_with_interpunction("elephant"))

while True:
    pig_latin_s_inputem()  
    skoncit = input("Chceš skončit (A = Ano)? ")
    if skoncit == "A":
        break
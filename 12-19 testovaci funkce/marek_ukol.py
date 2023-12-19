#.) Vytvořte funkci, která vezme slovo a vytvoří z něj slovo v Pig Latin
# a) Když slovo začíná samohláskou, přidá se na konec "way"
# b) Když slovo začíná souhláskou, souhláska se odebere, přidá se na konec 
# a za ní se přidá "ay"

#okud je v daném slově první písmeno velké, bude velké první písmeno i ve výsledku

def pig_latin(word):
    word = word.lower()
    
    first_letter = word[0] # první písmeno
    if first_letter in "aeiouy":
        word = word + "way"
        #return word + way
        return word
        
    else:
        word = word[1:] + first_letter + "ay" # [1:] od druhého 
    #return word[1:] + first_letter + "ay"
        return word
  



#______________________________________________________-
#print(pig_latin("ahoj"))
#print(pig_latin("počítač"))
#print(pig_latin("Počítač"))


   
     

def first_letter_capital(word):
    first_letter = word[0] 
    word = pig_latin(word)# volání funkce pig_latin

    if first_letter.isupper():
        return word.title()
    else:
        return word
    
    
print(first_letter_capital("FAhoj") == "Ahojfay")



#print(first_letter_capital(False))
def preklad_do_anglictiny(slovo):
    slovnik = {
        "jablko": "apple",
        "les": "forest",
        "láska": "love",
        "Vánoce": "Christmas"
    }
    if slovo in slovnik:
        return slovnik[slovo]
    else:
        return "Neumím přeložit"

def slovo_a_vypsani(prekladova_funkce, jmeno_prekladu):
    slovo = input("Zadej slovo, které mám zakódovat ")
    slovo = slovo.strip() # osekání mezer
    
    kodovane_slovo = prekladova_funkce(slovo)
    print("_____________________________________________________")
    print(f"Slovo k překladu je: {slovo} \n Zakódované slovo v {jmeno_prekladu} je:{kodovane_slovo}")




slovo_a_vypsani(first_letter_capital, "Pig Latin včetně velkých písmen")
slovo_a_vypsani(preklad_do_anglictiny, "angličtině")   


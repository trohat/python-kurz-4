# 1.) Vytvořte funkci, která vezme slovo a vytvoří z něj slovo v Pig Latin
# a) Když slovo začíná samohláskou, přidá se na konec "way"
# b) Když slovo začíná souhláskou, souhláska se odebere, přidá se na konec 
# a za ní se přidá "ay".  air => airway.   ear => earway  elephant => elephantway
# computer => omputercay.    cat => atcay.     papaya => apayapay

# 2.)Pokud je v daném slově první písmeno velké, bude velké první 
# písmeno i ve výsledkuComputer => Omputercay

# 3.)Slovo může mít na konci tečku nebo čárku -pokud tam je, bude na konci 
# i ve výsledku "computer," => "omputercay,"

print("Funkce na Pig Latin")
def pig_latin():
    
    word = input("Zadej slovo ")
    prvni_pismeno = word[0]
    if prvni_pismeno in "aeiouy": # operator in znamena jestli je obsažena samohláska
        new_word =  word + "way"
        
        print(new_word) # .capitalize() přidá velké písmeno na začátku
    else:
        new_word = word[1:] + prvni_pismeno + "ay" # vypsání řetězce, když není samohláska, vykrojení od 2 písmena do konce word[1:] 
        print(new_word)

    if prvni_pismeno.isupper():
        new_word = new_word.capitalize()
        print(new_word)
    else: 
        print(new_word)
    if word[-1] in ",.":
        new_word = new_word + word[-1] 
        
        print("handling interpunction", new_word)
    
        
pig_latin()
        
    
    
       


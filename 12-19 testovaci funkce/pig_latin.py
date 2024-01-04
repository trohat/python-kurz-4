from testy.testovani import test_equality

vowels = "aeiouy"

def pig_latin_word(word):
    word = word.lower()   
    first_letter = word[0] 
    if first_letter in vowels:   
        return word + "way"
    return word[1:] + first_letter + "ay"

def pig_latin_s_inputem():  
    slovo = input("Zadej slovo k překladu: ")
    vysledek = pig_latin_word(slovo)
    print(f"Překlad slova {slovo} do tajného jazyka je {vysledek}")

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


sentence = "Elephant Jumbo likes to eat bananas. Is he hungry today? Yes, he is."

def pig_latin_sentence(sentence):
    words = sentence.split()
    transformed_words = []
    for word in words:
        new_word = pig_latin_with_interpunction(word)    
        transformed_words.append(new_word)
    new_sentence = " ".join(transformed_words)
    return new_sentence

print(pig_latin_sentence(sentence))   

test_equality(pig_latin_word("eye"), "eyeway")
test_equality(pig_latin_word("Eye"), "Eyeway")
test_equality(pig_latin_with_capital("Eye"), "Eyeway")
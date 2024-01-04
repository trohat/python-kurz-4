#1.) Spočítejte, kolik je ve slově samohlásek "elephant" => 3
# Vytvoř si proměnnou, do které budeš ukládat samohlásky. 
# projdi slovo cyklem 
# podmínka, pokud je samohláska, ulož ji 
def count_vowels(word):
    box_for_vowels = 0 # začínám na 0 
    vowels = "aeiouy"
    for i in word:
        if i in vowels:
            box_for_vowels += 1 # připočítá se samohláska mužu vypsat i a vypíše samohlasky
              
    return box_for_vowels 


print("počet samophlásek ve slově ", count_vowels("ahojase"))


    
    


#2.) Spočítejte, kolikrát se ve slově vyskytuje sekvence "bob"'azcbobobegghakl' => 2
#




       #### funkce  ########
def look_for_bob(sentence):
  uloziste = 0
  for i in range(len(sentence)-2):
    if sentence[i:i+3] == "bob":  # krok o 3
      uloziste += 1
  return(uloziste)




look_for_bob("bobonbobobne")
look_for_bob("bobonbobobnebobob")



#3.) Napište funkci, která vezme řetězec a seřadí písmena v něm podle abecedy

veta = "ahoj pythone"
serazene_znaky = sorted(veta) # vytvoří seznam znaků 
# [' ', 'a', 'e', 'h', 'h', 'j', 'n', 'o', 'o', 'p', 't', 'y']

serazeny_retezec ="".join(serazene_znaky) # převede na řetězec

print(serazene_znaky)
print(serazeny_retezec)

##########                                funkce                         ##############
def serazeni_vety(veta):

  serazene_znaky = sorted(veta)
  serazeny_retezec ="".join(serazene_znaky)
  print(serazene_znaky)
  print(serazeny_retezec)
veta = "ahoj pythone"
serazeni_vety(veta)
   



#4.) Napište funkci, která vezme řetězec, a najde nejdelší podřetězec, ve kterém 
# jsou písmena řazená podle abecedy'azcbobobegghakl' => 'beggh'

#5.) Caesarova šifra - písmenka se posunou na další písmenko v abecedě
#a => b
#b => c
#c => d
#z => a

#ahoj => bipk (posun o jedna)
#ahoj => dkrm (posun o tři)

#6.) Ceasarova šifra naopak - rozkódovat


# a) Vytvoření slovníku
slovnik = {
    'hello': 'ahoj', 
    'world': 'svět', 
    'python': 'python', 
    'language': 'jazykx', 
    'code': 'kód'
}
print(slovnik)

#====================

# b) Přidání dalších slovíček
slovnik['computer'] = 'počítač'
slovnik['programming'] = 'programování'
print(slovnik)

#===============

# c) Tisk překladu nějakých slovíček
print("Překlad slova 'hello':", slovnik['hello'])
print("Překlad slova 'python':", slovnik['python'])

#==================

# d) Změna překladu slova
slovnik['language'] = 'jazyk'
print("Aktualizovaný překlad slova 'language':", slovnik['language'])

#=======================

# e) Zeptejte se, jestli je slovíčko v slovníku
dotaz_slovo1 = 'computer'
dotaz_slovo2 = 'program'

if dotaz_slovo1 in slovnik:
    print(f"Slovo '{dotaz_slovo1}' je v slovníku. Překlad: {slovnik[dotaz_slovo1]}")
else:
    print(f"Slovo '{dotaz_slovo1}' není v slovníku.")
    

if dotaz_slovo2 in slovnik:
    print(f"Slovo '{dotaz_slovo2}' je v slovníku. Překlad: {slovnik[dotaz_slovo2]}")
else:
    print(f"Slovo '{dotaz_slovo2}' není v slovníku.")
    
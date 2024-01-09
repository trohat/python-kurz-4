
seznam = [2, 5, 7, 3, 1, 4, 5, 9]

novy_seznam = []

for cislo in seznam:
    novy_seznam.append(cislo * cislo)   

print(novy_seznam)

# list comprehension
jeste_jeden_novy_seznam = [cislo * cislo for cislo in seznam]
print(jeste_jeden_novy_seznam)

retezec = "slon" 
novy_seznam = [ord(pismenko) for pismenko in retezec]  
print(novy_seznam)   

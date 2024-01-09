from pprint import pprint

seznam = [2, 5, 8, 6, 1, 8, 4, 5, 9, 12, 2, 5]

novy_seznam = []

for cislo in seznam:
    if cislo % 2 == 0:
        novy_seznam.append(cislo * cislo)   

print(novy_seznam)

# list comprehension
jeste_jeden_novy_seznam = [cislo * cislo for cislo in seznam if cislo % 2 == 0]
print(jeste_jeden_novy_seznam)

# set comprehension
neco_divneho = {cislo * cislo for cislo in seznam if cislo % 2 == 0}
print(neco_divneho)

# dict comprehension
slovnik = {cislo: cislo * cislo for cislo in seznam}
print(slovnik)

udaje_o_Petrovi = {
    "jmeno": "Petr",
    "oblibena barva": "oranžová",
    "oblibena kniha": "Deep Learning in Python",
    "oblíbené auto": "Toyota RAV4"
}

otoceny_slovnik = {dvojice[0] : dvojice[1] for dvojice in udaje_o_Petrovi.items()}
pprint(otoceny_slovnik)

for dvojice in udaje_o_Petrovi.items():
    print(dvojice)

anglickou_syntaxi_otoceny_slovnik = {hodnota : klic for klic, hodnota in udaje_o_Petrovi.items()}
pprint(anglickou_syntaxi_otoceny_slovnik)

anglickou_syntaxi_otoceny_slovnik = {v: k for k, v in udaje_o_Petrovi.items()}
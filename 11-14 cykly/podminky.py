
vek = int(input("Kolik ti je let? "))

if vek < 18:
    if vek < 5:
        print("Máme jahodové mléko...")
    elif vek < 10:
        print("Máme moc dobré kakao.")
    else: 
        print("Díš si pomerančový džus?")
    print("Máme borůvkovou limonádu.")
else:
    if vek < 30:
        print("Máme skvělý rum.")
    elif vek < 50:
        print("Máme červené i bílé, vyber si.")
    else:
        tvrde = input("Piješ tvrdý alkohol? Odpověz ano/ne")
        if tvrde == "ano":
            print("Máme kvalitní whisky!")
        else:
            print("Vídeňská káva se už připravuje")

    print("Máme skvělé plzeňské pivo.")

print("A máme hnusnou chemickou žlutou limonádu!!!")

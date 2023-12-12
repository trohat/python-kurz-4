
def mocnina(a, b):
    """
    vypočítá mocninu a na b
    """
    if b == 1:
        return a
    vysledek = mocnina(a, b-1)
    
    print(vysledek)
    return a * vysledek


print(mocnina(7, 5))
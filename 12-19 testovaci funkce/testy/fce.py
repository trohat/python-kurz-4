
from testovani import test_equality

def scitani(cislo1, cislo2):
    return cislo1 + cislo2



test_equality(scitani(5, 3), 8)
test_equality(scitani(5, 10), 11)
test_equality(scitani(5, 10), 15)
test_equality(scitani(5, 10), 17)
test_equality(5 < 3, True) 
test_equality(5 == 5, True)  

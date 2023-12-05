slovnik1 = {
    "slon":"elephant", 
    "opice":"monkey"
}

def pridej_do_slovniku_hada(sl):
    
    sl["had"] = "snake"
    return sl
    

pridej_do_slovniku_hada(slovnik1)
print(slovnik1)
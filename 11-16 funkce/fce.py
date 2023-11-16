
def privitani(jmeno, napoj):
    print(f"Ahoj {jmeno}, vítám tě na oslavě narozenin")
    print("Je tu zima, doufám, že máš teplé ponožky")
    if napoj == "pivo":
        print("Pivo je schované pod schodama, můžeš si tam jedno vzít")
        return
    
    print(f"Svůj oblíbený {napoj} si musíš najít.")
    
     
    print("Máme metaxu") # tohle se nikdy nestane
    return 2 * 9 + 6

#DRY = don't repeat yourself
muj_prvni_host = privitani("Pavle", "pivo")
privitani("Tomáši", "pivo")

print("Přípitek na oslavu")

privitani("Jirko", "rum")

privitani(napoj="víno", jmeno="Míšo")
#positional arguments
#keyword arguments


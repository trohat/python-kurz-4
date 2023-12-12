i = 0


def tiskni_ahoj():
    global i
    i += 1
    print(f"ahoj po {i}té")
    tiskni_ahoj()


tiskni_ahoj()

""" Nadefinujte slovník, kde klíče jsou jména lidí od vás z rodiny a 
hodnoty data jejich narození (vygooglete si, jak Python definuje datum).
Nechte uživatele zadat jméno někoho z rodiny, a vypočítejte, jak je starý.
"""



from datetime import datetime

family =  {
   "Alex": "1975-12-29",
   "Mary": "1985-11-07",
   "Piter": "2000-05-05",
   "Nicolas": "2010-06-28",
}

def find_age (birthday):
    birthday = datetime.strptime(birthday, "%Y-%M-%d")
    today = datetime.now()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

name = input("napis jmeno z rodiny: ")

name = name.strip().title()

if name in family:
    birthday = family[name]
    vek = find_age(birthday)
    print(f"{name} je {vek} let")
else:
    print(f"neni v rodine")
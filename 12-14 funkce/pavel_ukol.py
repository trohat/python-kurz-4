def print_items():
    
    for key, value in countries.items():
        print("slon", value.ljust(30), ':',"opice", key)
        
        


def print_one(countryname_or_capital):
    if (not exists_item(countryname_or_capital)):
        print(
            f"Polozka \"Nazev zeme\" = {countryname_or_capital} nebo \"Hlavni mesto\" = {countryname_or_capital} nebyla nalezena")
    else:
        key = search_item(countryname_or_capital)
        y = countries.get(key)

        print(key.ljust(30), ':', y)


def find_key(capital):
    item = capital.strip().title()
    for key, value in countries.items():
        if item == value:
            return key
    return ""


def exists_item(countryname_or_capital):
    if search_item(countryname_or_capital) != "":
        return True
    else:
        return False


def add_item(_countryname, _capital):
    if (exists_item(_countryname)):
        print(f"Nazev zeme {_countryname} jiz existuje")
        return

    if (exists_item(_capital)):
        print(f"Hlavni mesto {_capital} jiz existuje")
        return

    countries.update({_countryname.strip().title(): _capital.strip().title()})



def delete_item(_name):
    key = search_item(_name)

    if (key == ""):
        return False
    else:
        countries.pop(key)
        return True


def search_item(countryname_or_capital):
    item = countryname_or_capital.strip().title()

    if (item in countries):
        key = item
    else:
        key = find_key(item)

    return key


def replace_item(countryname_or_capital, newValue):
    key = search_item(countryname_or_capital)

    if (key == ""):
        return False
    else:
        countries[key] = newValue.strip().title()
        return True


countries = {
    "Belgium": "Brussels"
}

add_item("Afghanistan", "Kabul")
add_item("Albania", "Tirana (Tirane)")
add_item("Algeria", "Algiers")
add_item("Andorra", "Andorra la Vella")
add_item("Angola", "Luanda")
add_item("Antigua and Barbuda", "Saint John's")
add_item("Argentina", "Buenos Aires")
add_item("Armenia", "Yerevan")
add_item("Australia", "Canberra")
add_item("Austria", "Vienna")
add_item("Czech Republic", "Prague")

# add_item("Bahamas", "Nassau")
# add_item("Bahrain", "Manama")
# add_item("Bangladesh", "Dhaka")
# add_item("Barbados", "Bridgetown")
# add_item("Belarus", "Minsk")
# add_item("Belgium", "Brussels")
# add_item("Belize", "Belmopan")
# add_item("Benin", "Porto Novo")
# add_item("Bhutan", "Thimphu")
# add_item("Bolivia", "La Paz (administrative), Sucre (official)")
# add_item("Bosnia and Herzegovina", "Sarajevo")
# add_item("Botswana", "Gaborone")
# add_item("Brazil", "Brasilia")
# add_item("Brunei", "Bandar Seri Begawan")
# add_item("Bulgaria", "Sofia")
# add_item("Burkina Faso", "Ouagadougou")
# add_item("Burundi", "Gitega")
# add_item("Cambodia", "Phnom Penh")
# add_item("Cameroon", "Yaounde")
# add_item("Canada", "Ottawa")
# add_item("Cape Verde", "Praia")
# add_item("Central African Republic", "Bangui")
# add_item("Chad", "N'Djamena")
# add_item("Chile", "Santiago")
# add_item("China", "Beijing")
# add_item("Colombia", "Bogota")
# add_item("Comoros", "Moroni")
# add_item("Congo, Democratic Republic of the", "Kinshasa")
# add_item("Congo, Republic of the", "Brazzaville")
# add_item("Costa Rica", "San Jose")
# add_item("Côte d'Ivoire (Ivory Coast)", "Yamoussoukro[4]")
# add_item("Croatia", "Zagreb")
# add_item("Cuba", "Havana")
# add_item("Cyprus", "Nicosia")
# add_item("Denmark", "Copenhagen")
# add_item("Djibouti", "Djibouti")
# add_item("Dominica", "Roseau")
# add_item("Dominican Republic", "Santo Domingo")
# add_item("East Timor", "Dili")
# add_item("Ecuador", "Quito")
# add_item("Egypt", "Cairo")
# add_item("El Salvador", "San Salvador")
# add_item("England", "London")
# add_item("Equatorial Guinea", "Malabo")
# add_item("Eritrea", "Asmara")
# add_item("Estonia", "Tallinn")
# add_item("Eswatini (Swaziland)", "Mbabana")
# add_item("Ethiopia", "Addis Ababa")
# add_item("Federated States of Micronesia", "Palikir")
# add_item("Fiji", "Suva")
# add_item("Finland", "Helsinki")
# add_item("France", "Paris")
# add_item("Gabon", "Libreville")
# add_item("Gambia", "Banjul")
# add_item("Georgia", "Tbilisi")
# add_item("Germany", "Berlin")
# add_item("Ghana", "Accra")
# add_item("Greece", "Athens")
# add_item("Grenada", "Saint George's")
# add_item("Guatemala", "Guatemala City")
# add_item("Guinea", "Conakry")
# add_item("Guinea-Bissau", "Bissau")
# add_item("Guyana", "Georgetown")
# add_item("Haiti", "Port au Prince")
# add_item("Honduras", "Tegucigalpa")
# add_item("Hungary", "Budapest")
# add_item("Iceland", "Reykjavik")
# add_item("India", "New Delhi")
# add_item("Indonesia", "Jakarta[9]")
# add_item("Iran", "Tehran")
# add_item("Iraq", "Baghdad")
# add_item("Ireland", "Dublin")
# add_item("Israel", "Jerusalem")
# add_item("Italy", "Rome")
# add_item("Jamaica", "Kingston")
# add_item("Japan", "Tokyo")
# add_item("Jordan", "Amman")
# add_item("Kazakhstan", "Astana")
# add_item("Kenya", "Nairobi")
# add_item("Kiribati", "Tarawa Atoll")
# add_item("Kosovo", "Pristina")
# add_item("Kuwait", "Kuwait City")
# add_item("Kyrgyzstan", "Bishkek")
# add_item("aos", "Vientiane")
# add_item("atvia", "Riga")
# add_item("ebanon", "Beirut")
# add_item("esotho", "Maseru")
# add_item("iberia", "Monrovia")
# add_item("ibya", "Tripoii")
# add_item("iechtenstein", "Vaduz")
# add_item("ithuania", "Vinius")
# add_item("uxembourg", "Luxembourg")
# add_item("Madagascar", "Antananarivo")
# add_item("Malawi", "Lilongwe")
# add_item("Malaysia", "Kuala Lumpur")
# add_item("Maldives", "Male")
# add_item("Mali", "Bamako")
# add_item("Malta", "Valletta")
# add_item("Marshall Islands", "Majuro")
# add_item("Mauritania", "Nouakchott")
# add_item("Mauritius", "Port Louis")
# add_item("Mexico", "Mexico City")
# add_item("Moldova", "Chisinau")
# add_item("Monaco", "Monaco")
# add_item("Mongolia", "Ulaanbaatar")
# add_item("Montenegro", "Podgorica")
# add_item("Morocco", "Rabat")
# add_item("Mozambique", "Maputo")
# add_item("Myanmar (Burma)", "Nay Pyi Taw")
# add_item("Namibia", "Windhoek")
# add_item("Nauru", "No official capital")
# add_item("Nepal", "Kathmandu")
# add_item("Netherlands", "Amsterdam")
# add_item("New Zealand", "Wellington")
# add_item("Nicaragua", "Managua")
# add_item("Niger", "Niamey")
# add_item("Nigeria", "Abuja")
# add_item("North Korea", "Pyongyang")
# add_item("North Macedonia (Macedonia)[15]", "Skopje")
# add_item("Northern Ireland[16]", "Belfast")
# add_item("Norway", "Oslo")
# add_item("Oman", "Muscat")
# add_item("Pakistan", "Islamabad")
# add_item("Palau", "Melekeok")
# add_item("Palestine", "Jerusalem")
# add_item("Panama", "Panama City")
# add_item("Papua New Guinea", "Port Moresby")
# add_item("Paraguay", "Asuncion")
# add_item("Peru", "Lima")
# add_item("Philippines", "Manila")
# add_item("Poland", "Warsaw")
# add_item("Portugal", "Lisbon")
# add_item("Qatar", "Doha")
# add_item("Romania", "Bucharest")
# add_item("Russia", "Moscow")
# add_item("Rwanda", "Kigali")
# add_item("aint Kitts and Nevis", "Basseterre")
# add_item("Saint Lucia", "Castries")
# add_item("Saint Vincent and the Grenadines", "Kingstown")
# add_item("Samoa", "Apia")
# add_item("San Marino", "San Marino")
# add_item("Sao Tome and Principe", "Sao Tome")
# add_item("Saudi Arabia", "Riyadh")
# add_item("Scotland[19]", "Edinburgh")
# add_item("Senegal", "Dakar")
# add_item("Serbia", "Belgrade")
# add_item("Seychelles", "Victoria")
# add_item("Sierra Leone", "Freetown")
# add_item("Singapore", "Singapore")
# add_item("Slovakia", "Bratislava")
# add_item("Slovenia", "Ljubljana")
# add_item("Solomon Islands", "Honiara")
# add_item("Somalia", "Mogadishu")
# add_item("South Africa", "Pretoria, Bloemfontein, Cape Town")
# add_item("South Korea", "Seoul")
# add_item("South Sudan", "Juba")
# add_item("Spain", "Madrid")
# add_item("Sri Lanka", "Sri Jayawardenapura Kotte")
# add_item("Sudan", "Khartoum")
# add_item("Suriname", "Paramaribo")
# add_item("Sweden", "Stockholm")
# add_item("Switzerland", "Bern")
# add_item("Syria", "Damascus")
# add_item("Taiwan", "Taipei")
# add_item("Tajikistan", "Dushanbe")
# add_item("Tanzania", "Dodoma")
# add_item("Thailand", "Bangkok")
# add_item("Togo", "Lome")
# add_item("Tonga", "Nuku'alofa")
# add_item("Trinidad and Tobago", "Port of Spain")
# add_item("Tunisia", "Tunis")
# add_item("Turkey", "Ankara")
# add_item("Turkmenistan", "Ashgabat")
# add_item("Tuvalu", "Funafuti")
# add_item("Uganda", "Kampala")
# add_item("Ukraine", "Kyiv or Kiev")
# add_item("United Arab Emirates", "Abu Dhabi")
# add_item("United Kingdom", "London")
# add_item("United States", "Washington D.C.")
# add_item("Uruguay", "Montevideo")
# add_item("Uzbekistan", "Tashkent")
# add_item("Vanuatu", "Port Vila")
# add_item("Vatican City", "Vatican City")
# add_item("Venezuela", "Caracas")
# add_item("Vietnam", "Hanoi")
# add_item("Wales", "Cardiff")
# add_item("Yemen", "Sana'a")
# add_item("Zambia", "Lusaka")
# add_item("Zimbabwe", "Harare")

print("")
print("**********************************")
print("")
# pridani jiz existujiciho prvku
add_item("Austria", "Vienna")

print("")
print("**********************************")
print("")

# pridani dalsiho noveho prvku
add_item("Ceska republika", "Prah")

# Vypis seznamu
print_items()

print("")
print("**********************************")
print("")

if (not exists_item("Austriaa")):
    print("Austriaa - nenalezeno")

if (not exists_item("Vienna1")):
    print("Vienna1 - nenalezeno")

print("")
print("**********************************")
print("")

# smazani prvku

mesto = "Viennaaaaa"
if (not delete_item(mesto)):
    print(f"Polozka \"Nazev zeme\" {mesto} nebo \"Hlavni mesto\" {mesto} neexistuje")
else:
    print(f"Polozka \"Nazev zeme\" {mesto} nebo \"Hlavni mesto\" {mesto} byla smazana")

mesto = "Vienna"
if (not delete_item(mesto)):
    print(f"Polozka \"Nazev zeme\" {mesto} nebo \"Hlavni mesto\" {mesto} neexistuje")
else:
    print(f"Polozka \"Nazev zeme\" {mesto} nebo \"Hlavni mesto\" {mesto} byla smazana")

# pridani dalsiho noveho prvku
replace_item("Ceska republika", "Praha")

# Vypis seznamu
print("")
print("**********************************")
print("")
print_items()

print("")
print("**********************************")
print("")
print_one("Czech")
print_one("Prague")

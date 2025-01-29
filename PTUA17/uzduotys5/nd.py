# Įgyvendinkite paprastą žodyną, kuris saugo žodžius ir jų reikšmes. Leiskite vartotojui įvesti žodį ir atspausdinkite jo reikšmę.

# Užduoties instrukcijos:

# Iš anksto užpildykite žodyną keliais žodžiais ir jų reikšmėmis.

# Prašykite vartotojo įvesti žodį, kol ji nuspręs sustoti.

# Atspausdinkite žodžio reikšmę arba klaidą, jei žodyne nėra tokio žodžio.

# Pavyzdinis žodynas galėtų būti toks:

# dictionary = {
#     "obuolys": "vaisius, augantis ant medžių",
#     "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
#     "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
# }
# Pavyzdinė įvestis / išvestis:

# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): obuolys
# Žodžio obuolys reikšmė: vaisius, augantis ant medžių.
# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): automobilis
# Šio žodžio mūsų žodyne nėra.
# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): pabaiga


my_dictionary = {"obuolys": "vaisius, augantis ant medžių","knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius","kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
    user_input = input("Kurio zodzio reiksme norit suzinoti? obuolys/knyga/kompiuteris. Arba ivesk stop jei nori sustot ")
    if user_input == "stop":
        print("Stojam")
        break
    elif user_input == "obuolys":
        print(my_dictionary["obuolys"])
    elif user_input == "knyga":
        print(my_dictionary["knyga"])
    elif user_input == "kompiuteris":
        print(my_dictionary[user_input])
    else:
        print("nera")
#cia viskas veikia bet nera and ir not
ar_narys = input("Ar esate bibliotekos narys? (taip / ne) ".lower())

if ar_narys=="ne":
    print("Negali skolintis jokiu knygu")
elif ar_narys=="taip":
    amzius = int(input("Iveskite savo amziu "))
    if amzius<12:
        ar_lydi = (input("Ar jus lydi suauges asmuo? (taip/ne) ").lower())
    if amzius>=12 or ar_lydi=="taip":
            print("Galite skolintis visas knygas")
    else:
            print("gali skolintis tik is vaiku skyriaus")

